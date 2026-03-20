"""Tab 11: テーマ・スタイリング — Gradio のテーマシステムを解説するショーケース。"""

import gradio as gr


def build_tab() -> None:
    with gr.Tab("Tab 11: テーマ・スタイリング"):
        gr.Markdown("# テーマ・スタイリング")
        gr.Markdown(
            "Gradio のテーマシステムと CSS カスタマイズの概要を紹介します。"
            "テーマは `gr.Blocks(theme=...)` のようにアプリ全体に適用されるため、"
            "ここではカタログ表示・プレビュー・カスタマイズ方法の解説を行います。"
        )

        # ----------------------------------------------------------------
        # 1. プリセットテーマ一覧
        # ----------------------------------------------------------------
        gr.Markdown("### プリセットテーマ一覧")
        gr.Markdown(
            """\
Gradio 6 には以下のプリセットテーマが用意されています:

- **Default** (`gr.themes.Default()`) — 標準テーマ
- **Soft** (`gr.themes.Soft()`) — 柔らかい印象のテーマ
- **Glass** (`gr.themes.Glass()`) — ガラス風の透明感あるテーマ
- **Monochrome** (`gr.themes.Monochrome()`) — モノクロテーマ
- **Ocean** (`gr.themes.Ocean()`) — 海をイメージしたテーマ
- **Citrus** (`gr.themes.Citrus()`) — 柑橘系カラーのテーマ
- **Origin** (`gr.themes.Origin()`) — クラシックなテーマ"""
        )

        # ----------------------------------------------------------------
        # 2. テーマプレビュー
        # ----------------------------------------------------------------
        gr.Markdown("### テーマプレビュー")
        gr.Markdown("以下のコンポーネント群で現在のテーマの見た目を確認できます。")

        with gr.Row():
            with gr.Column():
                gr.Textbox(
                    label="テキスト入力",
                    value="サンプルテキスト",
                    interactive=True,
                )
                gr.Number(label="数値入力", value=42, interactive=True)
                gr.Slider(
                    label="スライダー",
                    minimum=0,
                    maximum=100,
                    value=50,
                    interactive=True,
                )
            with gr.Column():
                gr.Checkbox(label="チェックボックス", value=True, interactive=True)
                gr.Radio(
                    label="ラジオボタン",
                    choices=["選択肢A", "選択肢B", "選択肢C"],
                    value="選択肢A",
                    interactive=True,
                )
                gr.Dropdown(
                    label="ドロップダウン",
                    choices=["オプション1", "オプション2", "オプション3"],
                    value="オプション1",
                    interactive=True,
                )

        with gr.Row():
            gr.Button("Primary", variant="primary")
            gr.Button("Secondary", variant="secondary")
            gr.Button("Stop", variant="stop")

        # ----------------------------------------------------------------
        # 3. テーマのカスタマイズ解説
        # ----------------------------------------------------------------
        gr.Markdown("### テーマのカスタマイズ")
        gr.Markdown(
            """\
テーマは `gr.themes.Base()` を継承してカスタマイズできます:

```python
theme = gr.themes.Default(
    primary_hue="blue",
    secondary_hue="gray",
    neutral_hue="slate",
    font=gr.themes.GoogleFont("Noto Sans JP"),
)

with gr.Blocks(theme=theme) as demo:
    ...
```

`css_paths` パラメータでカスタム CSS ファイルを読み込むこともできます:
```python
demo.launch(css_paths=["custom.css"])
```"""
        )

        # ----------------------------------------------------------------
        # 4. CSS カスタマイズデモ
        # ----------------------------------------------------------------
        gr.Markdown("### CSS カスタマイズデモ")
        gr.HTML(
            """\
<div style="padding: 16px; background: linear-gradient(135deg, #667eea, #764ba2); border-radius: 12px; color: white;">
    <h3 style="margin: 0 0 8px;">カスタム CSS スタイリング</h3>
    <p style="margin: 0;">elem_id や elem_classes を使って個別のコンポーネントにCSSを適用できます。</p>
</div>"""
        )
        gr.Textbox(
            label="elem_id='custom-input'",
            elem_id="custom-input",
            value="カスタムスタイル適用例",
        )
