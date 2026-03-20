from __future__ import annotations

import gradio as gr


def build_tab() -> None:
    with gr.Tab("Tab 8: レイアウト・構造"):
        gr.Markdown(
            """## Tab 8: レイアウト・構造コンポーネント

Gradio 6 のレイアウト系コンポーネントを紹介します。
`Sidebar` / `Row` / `Column` / `Accordion` / `Group` / `render・unrender` の使い方を確認できます。
"""
        )

        # ── Sidebar ──────────────────────────────────────────
        gr.Markdown(
            """### Sidebar

`gr.Sidebar` はページ横にスライド表示される領域です。
`label` でタイトル、`open` で初期表示状態を指定します。
"""
        )

        with gr.Sidebar(label="サイドバーデモ", open=True) as sidebar:
            gr.Markdown("サイドバー内のコンテンツです。")
            sidebar_text = gr.Textbox(label="サイドバー入力")
            sidebar_output = gr.Textbox(label="入力の確認", interactive=False)
            sidebar_text.change(
                fn=lambda x: x,
                inputs=[sidebar_text],
                outputs=[sidebar_output],
            )

        toggle_btn = gr.Button("サイドバー開閉")
        # Note: Sidebar の開閉をプログラム的にトグルする API は現時点で
        # 提供されていない場合があります。ボタンは UI デモとして配置しています。

        # ── Row / Column ─────────────────────────────────────
        gr.Markdown(
            """### Row / Column

`gr.Row` は子要素を横並びに、`gr.Column` は縦並びに配置します。
`scale` で幅の比率、`min_width` で最小幅（px）を指定できます。
"""
        )

        with gr.Row():
            with gr.Column(scale=1, min_width=100):
                gr.Textbox(label="scale=1", value="狭い列", interactive=False)
            with gr.Column(scale=2, min_width=100):
                gr.Textbox(label="scale=2", value="中くらいの列", interactive=False)
            with gr.Column(scale=3, min_width=100):
                gr.Textbox(label="scale=3", value="広い列", interactive=False)

        # ── Accordion ────────────────────────────────────────
        gr.Markdown(
            """### Accordion

`gr.Accordion` は折りたたみ可能な領域です。
`open=True/False` で初期状態を指定でき、ネストも可能です。
"""
        )

        with gr.Accordion("外側アコーディオン", open=True):
            gr.Markdown("外側のコンテンツです。下にネストされたアコーディオンがあります。")
            with gr.Accordion("内側アコーディオン（ネスト）", open=False):
                gr.Markdown("内側のコンテンツです。クリックで展開されます。")

        # ── Group ────────────────────────────────────────────
        gr.Markdown(
            """### Group

`gr.Group` は複数コンポーネントを視覚的にひとまとめにします。
グループ内の要素間のマージンが詰まり、まとまった印象になります。
"""
        )

        with gr.Group():
            gr.Textbox(label="グループ内 A", value="まとめて表示", interactive=False)
            gr.Textbox(label="グループ内 B", value="まとめて表示", interactive=False)

        gr.Markdown("（比較用）グループなしの場合:")
        gr.Textbox(label="グループ外 A", value="個別に表示", interactive=False)
        gr.Textbox(label="グループ外 B", value="個別に表示", interactive=False)

        # ── render / unrender ────────────────────────────────
        gr.Markdown(
            """### render / unrender

`unrender()` でコンポーネントを一度取り外し、別の場所で `render()` して再配置できます。
以下の例では、テキストボックスを左列で定義した後 `unrender()` し、右列で `render()` しています。
"""
        )

        textbox = gr.Textbox(
            label="移動するコンポーネント",
            value="右列に表示されます",
            interactive=False,
        )
        textbox.unrender()

        with gr.Row():
            with gr.Column():
                gr.Markdown("**左列** — ここでは `unrender()` 済みのため表示されません。")
            with gr.Column():
                gr.Markdown("**右列** — `render()` によりここに表示されます。")
                textbox.render()
