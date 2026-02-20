from __future__ import annotations

import os

import gradio as gr
from dotenv import load_dotenv

from tabs.tab01_chat import build_tab as build_tab01
from tabs.tab02_chat_multimodal import build_tab as build_tab02
from tabs.tab03_chat_rich import build_tab as build_tab03
from tabs.tab04_chat_streaming import build_tab as build_tab04
from tabs.tab05_text_inputs import build_tab as build_tab05
from tabs.tab06_selection import build_tab as build_tab06
from tabs.tab07_media import build_tab as build_tab07
from tabs.tab08_image_editor import build_tab as build_tab08
from tabs.tab09_outputs_layout import build_tab as build_tab09
from tabs.tab10_apikey import build_tab as build_tab10


def build_app() -> gr.Blocks:
    load_dotenv()

    with gr.Blocks(title="Gradio 6 Playground") as demo:
        api_key_state = gr.State(value=None)
        session_id_state = gr.State(value=None)

        build_tab01(api_key_state, session_id_state)
        build_tab02()
        build_tab03()
        build_tab04()
        build_tab05()
        build_tab06()
        build_tab07()
        build_tab08()
        build_tab09()
        build_tab10(api_key_state, session_id_state)

    return demo


def main() -> None:
    demo = build_app()
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860)),
    )


if __name__ == "__main__":
    main()
