from __future__ import annotations

import base64
import io

import matplotlib
import matplotlib.pyplot as plt
import gradio as gr

matplotlib.use("Agg")


def _make_plot_html() -> str:
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.plot([1, 2, 3, 4, 5], [3, 1, 4, 1, 5], marker="o", color="#667eea", label="データA")
    ax.plot([1, 2, 3, 4, 5], [2, 4, 2, 5, 3], marker="s", color="#f093fb", label="データB")
    ax.set_title("Matplotlib グラフ")
    ax.legend()
    ax.grid(True, alpha=0.3)
    buf = io.BytesIO()
    fig.savefig(buf, format="png", bbox_inches="tight", dpi=100)
    plt.close(fig)
    buf.seek(0)
    b64 = base64.b64encode(buf.read()).decode()
    return f'<img src="data:image/png;base64,{b64}" alt="グラフ" style="max-width:100%;border-radius:8px;">'


def _add_text(history: list) -> list:
    history = list(history)
    history.append({"role": "user", "content": "テキストメッセージを見せて"})
    history.append(
        {
            "role": "assistant",
            "content": (
                "これは **Markdown** をサポートしたテキスト応答です。\n\n"
                "- リスト項目 1\n"
                "- リスト項目 2\n\n"
                "> 引用テキスト\n\n"
                "```python\nprint('Hello, Gradio 6!')\n```"
            ),
        }
    )
    return history


def _add_image(history: list) -> list:
    history = list(history)
    history.append({"role": "user", "content": "画像を見せて"})
    # Base64 で1×1ピクセルのカラフルな代替画像を使いサンプルHTMLを返す
    img_html = (
        '<div style="display:flex;gap:10px;flex-wrap:wrap;">'
        + "".join(
            f'<div style="width:80px;height:80px;background:{c};border-radius:8px;"></div>'
            for c in ["#ff6b6b", "#ffd93d", "#6bcb77", "#4d96ff", "#c77dff"]
        )
        + '<p style="width:100%;margin-top:8px;font-size:0.9em;color:#666;">カラーパレット（画像の代替デモ）</p>'
        "</div>"
    )
    history.append({"role": "assistant", "content": img_html})
    return history


def _add_plot(history: list) -> list:
    history = list(history)
    history.append({"role": "user", "content": "グラフを見せて"})
    history.append({"role": "assistant", "content": _make_plot_html()})
    return history


def _add_html(history: list) -> list:
    history = list(history)
    history.append({"role": "user", "content": "HTML コンテンツを見せて"})
    html = """<div style="background:linear-gradient(135deg,#667eea,#764ba2);padding:20px;border-radius:10px;color:white;">
<h3 style="margin:0 0 8px;">🎨 リッチ HTML コンテンツ</h3>
<p style="margin:0 0 12px;">Gradio 6 の Chatbot は HTML をレンダリングできます。</p>
<div style="display:flex;gap:8px;flex-wrap:wrap;">
  <span style="background:rgba(255,255,255,0.25);padding:4px 12px;border-radius:20px;font-size:0.85em;">タグA</span>
  <span style="background:rgba(255,255,255,0.25);padding:4px 12px;border-radius:20px;font-size:0.85em;">タグB</span>
  <span style="background:rgba(255,255,255,0.25);padding:4px 12px;border-radius:20px;font-size:0.85em;">タグC</span>
</div>
</div>"""
    history.append({"role": "assistant", "content": html})
    return history


def build_tab() -> None:
    with gr.Tab("Tab 3: リッチチャット"):
        gr.Markdown(
            """## Tab 3: リッチ応答チャットボット

使用コンポーネント: `gr.Chatbot(type="messages")`

- Gradio 6 の新形式 `type="messages"` を使用（OpenAI 互換の role/content 形式）
- ボタンを押してさまざまなリッチコンテンツを確認できます
- このタブは ADK 非使用のデモです
"""
        )
        chatbot = gr.Chatbot(height=400, label="リッチチャットボット")

        with gr.Row():
            btn_text = gr.Button("📝 テキスト", variant="secondary")
            btn_image = gr.Button("🖼️ 画像", variant="secondary")
            btn_plot = gr.Button("📊 グラフ", variant="secondary")
            btn_html = gr.Button("🎨 HTML", variant="secondary")
            btn_clear = gr.Button("🗑️ クリア", variant="stop")

        btn_text.click(_add_text, inputs=[chatbot], outputs=[chatbot])
        btn_image.click(_add_image, inputs=[chatbot], outputs=[chatbot])
        btn_plot.click(_add_plot, inputs=[chatbot], outputs=[chatbot])
        btn_html.click(_add_html, inputs=[chatbot], outputs=[chatbot])
        btn_clear.click(lambda: [], outputs=[chatbot])
