from __future__ import annotations

import gradio as gr


def _show_values(
    text: str,
    password: str,
    number: float,
    slider: float,
    code: str,
) -> str:
    lines = [
        f"**Textbox**: {text!r}",
        f"**Password** (長さのみ): {len(password or '')} 文字",
        f"**Number**: {number}",
        f"**Slider**: {slider}",
        f"**Code** (先頭 50 文字): {(code or '')[:50]!r}",
    ]
    return "\n\n".join(lines)


def build_tab() -> None:
    with gr.Tab("Tab 5: テキスト入力"):
        gr.Markdown(
            """## Tab 5: テキスト・数値入力コンポーネント

使用コンポーネント: `gr.Textbox` / `gr.Number` / `gr.Slider` / `gr.Code`

各コンポーネントに値を入力して「確認」ボタンを押すと、入力値が表示されます。
"""
        )

        with gr.Row():
            with gr.Column():
                text_input = gr.Textbox(
                    label="Textbox（複数行）",
                    placeholder="ここにテキストを入力…",
                    lines=3,
                )
                password_input = gr.Textbox(
                    label="Textbox（パスワード）",
                    placeholder="パスワード…",
                    type="password",
                )
                number_input = gr.Number(
                    label="Number",
                    value=42.0,
                    minimum=0,
                    maximum=1000,
                    step=0.5,
                )
                slider_input = gr.Slider(
                    label="Slider",
                    minimum=0,
                    maximum=100,
                    value=50,
                    step=1,
                    info="0〜100 の整数",
                )

            with gr.Column():
                code_input = gr.Code(
                    label="Code（Python）",
                    language="python",
                    value='def hello():\n    print("Hello, Gradio 6!")\n',
                )

        submit_btn = gr.Button("確認", variant="primary")
        output = gr.Markdown(label="入力値")

        submit_btn.click(
            _show_values,
            inputs=[text_input, password_input, number_input, slider_input, code_input],
            outputs=[output],
        )
