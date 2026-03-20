from __future__ import annotations

import gradio as gr


def _process_image(image):
    return image


def _process_audio(audio):
    if audio is None:
        return None
    return audio


def build_tab() -> None:
    with gr.Tab("Tab 7: メディア"):
        gr.Markdown(
            """## Tab 7: メディア入出力コンポーネント

使用コンポーネント: `gr.Image` / `gr.Audio` / `gr.Video` / `gr.File` / `gr.Gallery`

各コンポーネントにファイルをアップロードして動作を確認できます。
"""
        )

        with gr.Tabs():
            with gr.Tab("Image"):
                gr.Markdown("画像をアップロードまたはウェブカメラで撮影できます。「送信」後にそのまま出力されます。")
                with gr.Row():
                    image_input = gr.Image(
                        label="入力画像",
                        type="filepath",
                        sources=["upload", "webcam", "clipboard"],
                    )
                    image_output = gr.Image(label="出力画像（エコー）")
                gr.Button("送信", variant="primary").click(
                    _process_image, inputs=[image_input], outputs=[image_output]
                )

            with gr.Tab("Audio"):
                gr.Markdown("音声をアップロードまたはマイクで録音できます。「送信」後にそのまま再生されます。")
                with gr.Row():
                    audio_input = gr.Audio(
                        label="入力音声",
                        sources=["upload", "microphone"],
                    )
                    audio_output = gr.Audio(label="出力音声（エコー）")
                gr.Button("送信", variant="primary").click(
                    _process_audio, inputs=[audio_input], outputs=[audio_output]
                )

            with gr.Tab("Video"):
                gr.Markdown("動画をアップロードできます。")
                video_input = gr.Video(label="動画")

            with gr.Tab("File"):
                gr.Markdown("任意のファイルをアップロードできます。")
                file_input = gr.File(
                    label="ファイルアップロード",
                    file_count="multiple",
                )
                file_output = gr.JSON(label="ファイル情報")

                def _file_info(files):
                    if not files:
                        return {}
                    if isinstance(files, list):
                        return [{"name": f, "type": "file"} for f in files]
                    return {"name": files, "type": "file"}

                file_input.change(_file_info, inputs=[file_input], outputs=[file_output])

            with gr.Tab("Gallery"):
                gr.Markdown("複数画像をギャラリー形式で表示します。")
                gallery_input = gr.File(
                    label="画像をアップロード（複数可）",
                    file_count="multiple",
                    file_types=["image"],
                )
                gallery_output = gr.Gallery(
                    label="ギャラリー",
                    columns=3,
                    height="auto",
                )

                def _to_gallery(files):
                    if not files:
                        return []
                    if isinstance(files, list):
                        return files
                    return [files]

                gallery_input.change(_to_gallery, inputs=[gallery_input], outputs=[gallery_output])
