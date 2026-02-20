from __future__ import annotations

import time

import gradio as gr

_DUMMY_RESPONSES = [
    "こんにちは！これはストリーミングのデモです。",
    "Gradio 6 では `yield` を使ってテキストを少しずつ返せます。",
    "ストリーミングにより、長い応答でもリアルタイムに表示されます。",
    "実際の LLM 応答もこの仕組みで逐次表示できます。",
]


def _stream_chat(message: str, history: list) -> str:
    # メッセージに応じて返答を選択
    idx = len(history) % len(_DUMMY_RESPONSES)
    response = _DUMMY_RESPONSES[idx]

    accumulated = ""
    for char in response:
        accumulated += char
        time.sleep(0.04)
        yield accumulated


def build_tab() -> None:
    with gr.Tab("Tab 4: ストリーミングチャット"):
        gr.Markdown(
            """## Tab 4: ストリーミングチャット

使用コンポーネント: `gr.ChatInterface(type="messages")` + `yield`

- `fn` が `yield` でテキストを少しずつ返すとリアルタイム表示されます
- `type="messages"` で OpenAI 互換のメッセージ形式を使用
- このタブは ADK 非使用のダミーストリームデモです
"""
        )
        gr.ChatInterface(
            fn=_stream_chat,
            title="",
            description="何かメッセージを送ると、文字が1文字ずつストリーミング表示されます。",
        )
