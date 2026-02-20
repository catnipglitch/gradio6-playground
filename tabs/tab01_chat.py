from __future__ import annotations

import gradio as gr

from .adk_utils import ensure_session_id, resolve_api_key, run_prompt


async def _chat(
    message: str,
    history: list[tuple[str, str]],
    api_key: str | None,
    session_id: str | None,
) -> tuple[str, str]:
    resolved_session_id = ensure_session_id(session_id)
    resolved_key = resolve_api_key(api_key)
    if not resolved_key:
        return "APIキーが未設定です。Tab 10 で入力するか環境変数を設定してください。", resolved_session_id

    try:
        response = await run_prompt(
            message,
            resolved_key,
            session_id=resolved_session_id,
        )
    except Exception:
        return "エラーが発生しました。しばらくしてからお試しください。", resolved_session_id

    return response, resolved_session_id


def build_tab(api_key_state: gr.State, session_id_state: gr.State) -> None:
    with gr.Tab("Tab 1: チャットテスト"):
        gr.Markdown("Google ADK を使ったチャットテストです。")
        gr.ChatInterface(
            fn=_chat,
            additional_inputs=[api_key_state, session_id_state],
            additional_outputs=[session_id_state],
        )
