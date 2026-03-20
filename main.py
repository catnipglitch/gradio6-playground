from __future__ import annotations

import os

import gradio as gr
from dotenv import load_dotenv

from tabs.tab01_chat import build_tab as build_tab01
from tabs.tab02_chat_showcase import build_tab as build_tab02
from tabs.tab03_text_inputs import build_tab as build_tab03
from tabs.tab04_selection import build_tab as build_tab04
from tabs.tab05_media import build_tab as build_tab05
from tabs.tab06_image_editor import build_tab as build_tab06
from tabs.tab07_data_outputs import build_tab as build_tab07
from tabs.tab08_layout import build_tab as build_tab08
from tabs.tab09_events_timer import build_tab as build_tab09
from tabs.tab10_new_v6 import build_tab as build_tab10
from tabs.tab11_theming import build_tab as build_tab11
from tabs.tab12_apikey import build_tab as build_tab12


def build_app() -> gr.Blocks:
    load_dotenv()

    with gr.Blocks(title="Gradio 6.9 Playground") as demo:
        api_key_state = gr.State(value=None)
        session_id_state = gr.State(value=None)

        with gr.Sidebar(label="Gradio 6.9 Playground"):
            gr.Markdown(
                f"**Gradio 6.9 Playground**\n\n"
                f"Gradio バージョン: `{gr.__version__}`\n\n"
                f"12 タブ構成で Gradio 6 の機能をショーケースします。"
            )

        build_tab01(api_key_state, session_id_state)
        build_tab02()
        build_tab03()
        build_tab04()
        build_tab05()
        build_tab06()
        build_tab07()
        build_tab08()
        build_tab09()
        build_tab10()
        build_tab11()
        build_tab12(api_key_state, session_id_state)

    return demo


def main() -> None:
    demo = build_app()
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 7860)),
    )


if __name__ == "__main__":
    main()
