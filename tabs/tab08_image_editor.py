from __future__ import annotations

import gradio as gr


def _apply_edit(editor_value):
    if editor_value is None:
        return None
    # composite はブラシ描画やレイヤーを合成した最終画像
    composite = editor_value.get("composite")
    return composite


def _update_brush_size(size: int):
    return gr.update(brush=gr.Brush(default_size=size))


def build_tab() -> None:
    with gr.Tab("Tab 8: 画像エディタ"):
        gr.Markdown(
            """## Tab 8: ImageEditor 2D

使用コンポーネント: `gr.ImageEditor` / `gr.Brush` / `gr.Eraser` / `gr.Slider`

- **ブラシ**: 左上のツールバーでブラシを選択して描画
- **消しゴム**: ツールバーで消しゴムを選択して消去
- **クロップ**: ツールバーでクロップモードに切り替え
- **ブラシサイズ**: 下のスライダーでリアルタイム変更
- 「適用」ボタンで合成画像を右の出力に表示
"""
        )

        with gr.Row():
            with gr.Column(scale=2):
                editor = gr.ImageEditor(
                    label="キャンバス（800×500）",
                    canvas_size=(800, 500),
                    brush=gr.Brush(
                        default_size=10,
                        colors=["#000000", "#ff0000", "#00bb00", "#0000ff", "#ff9900"],
                        default_color="#000000",
                    ),
                    eraser=gr.Eraser(default_size=20),
                )

            with gr.Column(scale=1):
                output_image = gr.Image(label="適用後の画像")

        with gr.Row():
            brush_slider = gr.Slider(
                label="ブラシサイズ",
                minimum=1,
                maximum=100,
                value=10,
                step=1,
            )
            apply_btn = gr.Button("適用", variant="primary")

        brush_slider.change(
            _update_brush_size,
            inputs=[brush_slider],
            outputs=[editor],
        )

        apply_btn.click(
            _apply_edit,
            inputs=[editor],
            outputs=[output_image],
        )
