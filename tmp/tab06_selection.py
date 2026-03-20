from __future__ import annotations

import gradio as gr


def _show_values(
    checkbox: bool,
    checkbox_group: list[str],
    radio: str,
    dropdown: str,
    color: str,
) -> str:
    lines = [
        f"**Checkbox**: {checkbox}",
        f"**CheckboxGroup**: {checkbox_group}",
        f"**Radio**: {radio!r}",
        f"**Dropdown**: {dropdown!r}",
        f"**ColorPicker**: `{color}`",
    ]
    return "\n\n".join(lines)


def build_tab() -> None:
    with gr.Tab("Tab 6: 選択入力"):
        gr.Markdown(
            """## Tab 6: 選択入力コンポーネント

使用コンポーネント: `gr.Checkbox` / `gr.CheckboxGroup` / `gr.Radio` / `gr.Dropdown` / `gr.ColorPicker`

各コンポーネントを操作して「確認」ボタンを押すと、選択値が表示されます。
"""
        )

        with gr.Row():
            with gr.Column():
                checkbox_input = gr.Checkbox(
                    label="Checkbox",
                    value=True,
                    info="オン/オフを切り替えられます",
                )
                checkbox_group_input = gr.CheckboxGroup(
                    label="CheckboxGroup",
                    choices=["Python", "TypeScript", "Rust", "Go"],
                    value=["Python"],
                    info="複数選択できます",
                )
                radio_input = gr.Radio(
                    label="Radio",
                    choices=["小", "中", "大"],
                    value="中",
                    info="いずれか一つを選択",
                )

            with gr.Column():
                dropdown_input = gr.Dropdown(
                    label="Dropdown",
                    choices=["オプション A", "オプション B", "オプション C", "オプション D"],
                    value="オプション A",
                    info="プルダウンで選択",
                )
                color_input = gr.ColorPicker(
                    label="ColorPicker",
                    value="#667eea",
                    info="カラーピッカーで色を選択",
                )

        submit_btn = gr.Button("確認", variant="primary")
        output = gr.Markdown(label="選択値")

        submit_btn.click(
            _show_values,
            inputs=[
                checkbox_input,
                checkbox_group_input,
                radio_input,
                dropdown_input,
                color_input,
            ],
            outputs=[output],
        )
