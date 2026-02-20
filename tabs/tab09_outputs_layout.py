from __future__ import annotations

import base64
import io

import matplotlib
import matplotlib.pyplot as plt
import gradio as gr

matplotlib.use("Agg")


def _make_plot():
    fig, axes = plt.subplots(1, 2, figsize=(8, 3))
    axes[0].bar(["A", "B", "C", "D"], [3, 7, 2, 5], color=["#ff6b6b", "#ffd93d", "#6bcb77", "#4d96ff"])
    axes[0].set_title("棒グラフ")
    axes[1].pie([30, 25, 20, 15, 10], labels=["A", "B", "C", "D", "E"], autopct="%1.0f%%")
    axes[1].set_title("円グラフ")
    fig.tight_layout()
    return fig


_SAMPLE_JSON = {
    "app": "Gradio 6 Playground",
    "tabs": [
        {"id": 1, "name": "チャットテスト", "adk": True},
        {"id": 2, "name": "マルチモーダル", "adk": False},
        {"id": 9, "name": "出力・レイアウト", "adk": False},
    ],
    "version": "0.1.0",
}

_SAMPLE_LABEL = {"猫": 0.72, "犬": 0.18, "鳥": 0.07, "魚": 0.03}

_SAMPLE_HIGHLIGHTED = [
    ("これは", None),
    ("重要な", "重要"),
    ("テキストです。", None),
    ("Gradio 6", "新機能"),
    ("では", None),
    ("ハイライト表示", "強調"),
    ("が簡単にできます。", None),
]


def build_tab() -> None:
    with gr.Tab("Tab 9: 出力・レイアウト"):
        gr.Markdown(
            """## Tab 9: 出力コンポーネント & レイアウト

使用コンポーネント: `gr.Label` / `gr.HighlightedText` / `gr.JSON` / `gr.Plot` / `gr.Accordion` / `gr.Group`

Gradio 6 のさまざまな出力・レイアウトコンポーネントをデモします。
"""
        )

        with gr.Row():
            with gr.Column():
                gr.Markdown("### Label（分類結果）")
                gr.Label(
                    value=_SAMPLE_LABEL,
                    label="画像分類スコア（サンプル）",
                    num_top_classes=4,
                )

            with gr.Column():
                gr.Markdown("### HighlightedText（スパンハイライト）")
                gr.HighlightedText(
                    value=_SAMPLE_HIGHLIGHTED,
                    label="ハイライトテキスト",
                    color_map={"重要": "red", "新機能": "green", "強調": "blue"},
                )

        gr.Markdown("---")

        with gr.Row():
            with gr.Column():
                gr.Markdown("### JSON（ツリー表示）")
                gr.JSON(value=_SAMPLE_JSON, label="JSON データ")

            with gr.Column():
                gr.Markdown("### Plot（matplotlib）")
                plot_component = gr.Plot(label="グラフ")
                gr.Button("グラフを描画", variant="primary").click(
                    _make_plot, outputs=[plot_component]
                )

        gr.Markdown("---")
        gr.Markdown("### Accordion（折りたたみ）")

        with gr.Accordion("クリックして開く: Accordion デモ", open=False):
            gr.Markdown(
                "Accordion 内のコンテンツです。`open=False` で最初は閉じた状態になります。"
            )
            with gr.Row():
                gr.Textbox(label="Accordion 内の入力", placeholder="ここに入力")
                gr.Markdown("Accordion 内には任意のコンポーネントを配置できます。")

        with gr.Accordion("もう一つの Accordion（最初から開く）", open=True):
            gr.Markdown("こちらは `open=True` で最初から展開されています。")

        gr.Markdown("---")
        gr.Markdown("### Group（グループ化）")

        with gr.Group():
            gr.Markdown("**Group** でコンポーネントを視覚的にまとめられます。")
            with gr.Row():
                gr.Textbox(label="グループ内 入力A", scale=2)
                gr.Textbox(label="グループ内 入力B", scale=2)
                gr.Button("グループ内ボタン", scale=1)
