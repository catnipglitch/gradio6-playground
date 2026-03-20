from __future__ import annotations

import gradio as gr

from .adk_utils import ensure_session_id, run_prompt


async def _test_key(
    key_input: str,
    current_key: str | None,
    session_id: str | None,
) -> tuple[str, str | None, str]:
    if not key_input:
        return "APIキーを入力してください。", current_key, ensure_session_id(session_id)

    resolved_session_id = ensure_session_id(session_id)
    try:
        response = await run_prompt(
            "Reply with OK.",
            key_input,
            session_id=resolved_session_id,
        )
    except Exception:
        return "認証に失敗しました。APIキーを確認してください。", current_key, resolved_session_id

    if "OK" in response:
        return "認証に成功しました。", key_input, resolved_session_id
    return "認証に失敗しました。APIキーを確認してください。", current_key, resolved_session_id


def build_tab(api_key_state: gr.State, session_id_state: gr.State) -> None:
    with gr.Tab("Tab 10: APIキー設定"):
        gr.Markdown("Gemini APIキーを入力し、認証テストを行います。")
        key_input = gr.Textbox(
            label="APIキー",
            placeholder="GEMINI_API_KEY",
            type="password",
        )
        test_button = gr.Button("認証テスト")
        status = gr.Markdown()

        test_button.click(
            _test_key,
            inputs=[key_input, api_key_state, session_id_state],
            outputs=[status, api_key_state, session_id_state],
        )

        gr.Markdown(
            "現在のキー優先順位: Tab 10 入力 > 環境変数 `GEMINI_API_KEY`。"
        )
