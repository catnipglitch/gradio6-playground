from __future__ import annotations

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import gradio as gr


def _make_plot():
    fig, axes = plt.subplots(1, 2, figsize=(8, 3))
    axes[0].bar(
        ["A", "B", "C", "D"],
        [3, 7, 2, 5],
        color=["#ff6b6b", "#ffd93d", "#6bcb77", "#4d96ff"],
    )
    axes[0].set_title("棒グラフ")
    axes[1].pie(
        [30, 25, 20, 15, 10],
        labels=["A", "B", "C", "D", "E"],
        autopct="%1.0f%%",
    )
    axes[1].set_title("円グラフ")
    fig.tight_layout()
    return fig


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

_SAMPLE_JSON = {
    "app": "Gradio 6 Playground",
    "tabs": [
        {"id": 1, "name": "チャットテスト", "adk": True},
        {"id": 2, "name": "マルチモーダル", "adk": False},
        {"id": 7, "name": "データ表示・出力", "adk": False},
    ],
    "version": "0.1.0",
}

_SAMPLE_DATAFRAME = {
    "headers": ["名前", "年齢", "職業", "スコア", "合格"],
    "data": [
        ["田中太郎", 28, "エンジニア", 92.5, True],
        ["佐藤花子", 34, "デザイナー", 87.3, True],
        ["鈴木一郎", 45, "マネージャー", 78.1, True],
        ["高橋美咲", 23, "インターン", 65.0, False],
        ["渡辺健太", 31, "データサイエンティスト", 95.8, True],
    ],
}

_SAMPLE_HTML = """\
<div style="font-family: sans-serif; padding: 16px; border: 2px solid #4d96ff; border-radius: 12px; background: linear-gradient(135deg, #f0f4ff, #e8f0fe);">
  <h3 style="color: #1a73e8; margin-top: 0;">Gradio 6 HTML デモ</h3>
  <p style="color: #333;">これは <code>gr.HTML</code> コンポーネントで描画されたカスタム HTML です。</p>
  <ul style="color: #555;">
    <li>リッチなスタイリングが可能</li>
    <li>インラインCSS でレイアウトを自由に制御</li>
    <li>外部ライブラリ不要で表現力のあるUIを構築</li>
  </ul>
  <div style="display: flex; gap: 8px; margin-top: 12px;">
    <span style="background: #ff6b6b; color: white; padding: 4px 12px; border-radius: 16px; font-size: 14px;">タグA</span>
    <span style="background: #6bcb77; color: white; padding: 4px 12px; border-radius: 16px; font-size: 14px;">タグB</span>
    <span style="background: #4d96ff; color: white; padding: 4px 12px; border-radius: 16px; font-size: 14px;">タグC</span>
  </div>
</div>
"""

_SAMPLE_PARAMS = {
    "value": {
        "type": "str",
        "default": '""',
        "description": "コンポーネントの初期値",
    },
    "label": {
        "type": "str | None",
        "default": "None",
        "description": "表示ラベル",
    },
    "visible": {
        "type": "bool",
        "default": "True",
        "description": "コンポーネントの表示/非表示",
    },
    "interactive": {
        "type": "bool",
        "default": "True",
        "description": "ユーザー操作を受け付けるかどうか",
    },
    "elem_id": {
        "type": "str | None",
        "default": "None",
        "description": "HTML の id 属性",
    },
}


def build_tab() -> None:
    with gr.Tab("Tab 7: データ表示・出力"):
        gr.Markdown(
            """## Tab 7: データ表示・出力コンポーネント

使用コンポーネント: `gr.Label` / `gr.HighlightedText` / `gr.JSON` / `gr.Plot` / `gr.Dataframe` / `gr.HTML` / `gr.ParamViewer`

Gradio 6 の出力・データ表示系コンポーネントを集約したショーケースです。
"""
        )

        # -- Section 1: Label & HighlightedText --
        gr.Markdown("### Label & HighlightedText")
        with gr.Row():
            with gr.Column():
                gr.Label(
                    value=_SAMPLE_LABEL,
                    label="画像分類スコア（サンプル）",
                    num_top_classes=4,
                )

            with gr.Column():
                gr.HighlightedText(
                    value=_SAMPLE_HIGHLIGHTED,
                    label="ハイライトテキスト",
                    color_map={"重要": "red", "新機能": "green", "強調": "blue"},
                )

        gr.Markdown("---")

        # -- Section 2: JSON & Plot --
        gr.Markdown("### JSON & Plot")
        with gr.Row():
            with gr.Column():
                gr.JSON(value=_SAMPLE_JSON, label="JSON データ")

            with gr.Column():
                plot_component = gr.Plot(label="matplotlib グラフ")
                gr.Button("グラフを描画", variant="primary").click(
                    _make_plot, outputs=[plot_component]
                )

        gr.Markdown("---")

        # -- Section 3: Dataframe --
        gr.Markdown("### Dataframe（テーブル表示）")
        with gr.Row():
            with gr.Column():
                gr.Dataframe(
                    value=_SAMPLE_DATAFRAME["data"],
                    headers=_SAMPLE_DATAFRAME["headers"],
                    label="サンプルデータテーブル",
                    row_count=(5, "fixed"),
                    column_count=(5, "fixed"),
                    interactive=False,
                )

        gr.Markdown("---")

        # -- Section 4: HTML --
        gr.Markdown("### HTML（カスタム HTML 描画）")
        with gr.Row():
            with gr.Column():
                gr.HTML(value=_SAMPLE_HTML, label="HTML スニペット")

        gr.Markdown("---")

        # -- Section 5: ParamViewer --
        gr.Markdown("### ParamViewer（パラメータ情報表示）")
        with gr.Row():
            with gr.Column():
                gr.ParamViewer(
                    value=_SAMPLE_PARAMS,
                    header="gr.Textbox のパラメータ（サンプル）",
                )
