from __future__ import annotations

import asyncio
import os
import uuid
from contextlib import contextmanager, nullcontext
from typing import Optional

from google.adk.agents import LlmAgent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

APP_NAME = "gradio6-playground"
MODEL_NAME = "gemini-2.0-flash"

_SESSION_SERVICE = InMemorySessionService()
_CREATED_SESSIONS: set[tuple[str, str]] = set()


def resolve_api_key(session_key: Optional[str]) -> Optional[str]:
    if session_key:
        return session_key
    return os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")


def ensure_session_id(session_id: Optional[str]) -> str:
    if session_id:
        return session_id
    return uuid.uuid4().hex


async def ensure_session(user_id: str, session_id: str) -> None:
    key = (user_id, session_id)
    if key in _CREATED_SESSIONS:
        return

    result = _SESSION_SERVICE.create_session(
        app_name=APP_NAME,
        user_id=user_id,
        session_id=session_id,
    )
    if asyncio.iscoroutine(result):
        await result
    _CREATED_SESSIONS.add(key)


@contextmanager
def _temporary_api_key(api_key: str):
    previous = os.environ.get("GOOGLE_API_KEY")
    os.environ["GOOGLE_API_KEY"] = api_key
    try:
        yield
    finally:
        if previous is None:
            os.environ.pop("GOOGLE_API_KEY", None)
        else:
            os.environ["GOOGLE_API_KEY"] = previous


async def run_prompt(
    prompt: str,
    api_key: Optional[str],
    *,
    session_id: str,
    user_id: str = "gradio_user",
) -> str:
    if not prompt:
        return ""

    await ensure_session(user_id=user_id, session_id=session_id)

    agent = LlmAgent(
        name="chat_agent",
        model=MODEL_NAME,
        instruction="You are a helpful assistant.",
    )
    runner = Runner(
        agent=agent,
        app_name=APP_NAME,
        session_service=_SESSION_SERVICE,
    )
    content = types.Content(role="user", parts=[types.Part(text=prompt)])

    response_text = ""
    context = _temporary_api_key(api_key) if api_key else nullcontext()
    with context:
        async for event in runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=content,
        ):
            if event.is_final_response() and event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        response_text = part.text
    return response_text or "(no response)"
