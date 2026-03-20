from __future__ import annotations

import os
import tempfile

import gradio as gr


def _create_sample_file() -> str:
    path = os.path.join(tempfile.gettempdir(), "sample.txt")
    with open(path, "w") as f:
        f.write("Gradio 6.9 Playground - サンプルファイル\n")
    return path


def _annotate_image(img):
    if img is None:
        return None
    h, w = img.shape[:2]
    annotations = [
        ((int(w * 0.1), int(h * 0.1), int(w * 0.5), int(h * 0.5)), "領域A"),
        ((int(w * 0.5), int(h * 0.3), int(w * 0.9), int(h * 0.8)), "領域B"),
    ]
    return (img, annotations)


def build_tab():
    with gr.Tab("Tab 10: v6 新コンポーネント"):
        gr.Markdown(
            "## v6 新コンポーネント ショーケース\n\n"
            "Gradio 6 で追加・強化されたコンポーネントを紹介します。"
        )

        # --- FileExplorer ---
        gr.Markdown("### FileExplorer")
        gr.Markdown("`gr.FileExplorer` でサーバー側のファイルを閲覧できます。")
        file_explorer = gr.FileExplorer(
            label="ファイルエクスプローラー",
            root_dir="./tabs",
            glob="**/*.py",
        )
        selected_file = gr.Textbox(label="選択されたファイル")
        file_explorer.change(
            lambda x: str(x), inputs=file_explorer, outputs=selected_file
        )

        # --- DownloadButton ---
        gr.Markdown("### DownloadButton")
        gr.Markdown("`gr.DownloadButton` でファイルをダウンロードできます。")
        gr.DownloadButton(
            label="サンプルファイルをダウンロード", value=_create_sample_file()
        )

        # --- ParamViewer ---
        gr.Markdown("### ParamViewer")
        gr.Markdown(
            "`gr.ParamViewer` でコンポーネントのパラメータを表示できます。"
        )
        gr.ParamViewer(
            value={
                "text": {
                    "type": "str",
                    "default": '""',
                    "description": "テキスト入力値",
                },
                "lines": {
                    "type": "int",
                    "default": "1",
                    "description": "表示行数",
                },
                "placeholder": {
                    "type": "str",
                    "default": "None",
                    "description": "プレースホルダーテキスト",
                },
            },
            header="gr.Textbox パラメータ例",
        )

        # --- AnnotatedImage ---
        gr.Markdown("### AnnotatedImage")
        gr.Markdown(
            "`gr.AnnotatedImage` でバウンディングボックスやマスク付き画像を表示できます。"
        )
        gr.Markdown("画像をアップロードすると、サンプルのアノテーションが追加されます。")

        img_input = gr.Image(label="入力画像", type="numpy")
        annotated_output = gr.AnnotatedImage(label="アノテーション付き画像")

        img_input.change(
            _annotate_image, inputs=img_input, outputs=annotated_output
        )
