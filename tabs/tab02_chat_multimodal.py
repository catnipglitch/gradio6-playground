from __future__ import annotations

import gradio as gr


def _chat(message: dict, history: list) -> str:
    text = message.get("text", "") or ""
    files = message.get("files", []) or []

    parts: list[str] = []
    if text:
        parts.append(f"テキスト: 「{text}」")
    if files:
        parts.append(f"ファイル数: {len(files)} 件")
        for f in files:
            parts.append(f"  - `{f}`")

    if not parts:
        return "（空のメッセージ）"

    return "\n".join(parts)


def build_tab() -> None:
    with gr.Tab("Tab 2: マルチモーダルチャット"):
        gr.Markdown(
            """## Tab 2: マルチモーダルチャット

使用コンポーネント: `gr.ChatInterface(multimodal=True)`

- テキストと画像・ファイルを同時に送信できます
- `message` 引数は `{"text": str, "files": list[str]}` の形式で渡されます
- このタブは ADK 非使用のエコーデモです
"""
        )
        gr.ChatInterface(
            fn=_chat,
            multimodal=True,
        )
