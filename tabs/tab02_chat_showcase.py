from __future__ import annotations

import base64
import io
import time

import matplotlib
import matplotlib.pyplot as plt
import gradio as gr

matplotlib.use("Agg")

# ---------------------------------------------------------------------------
# マルチモーダルチャット (旧 Tab 2)
# ---------------------------------------------------------------------------


def _chat_multimodal(message: dict, history: list) -> str:
    text = message.get("text", "") or ""
    files = message.get("files", []) or []

    parts: list[str] = []
    if text:
        parts.append(f"テキスト: 「{text}」")
    if files:
        parts.append(f"ファイル数: {len(files)} 件")
        for f in files:
            parts.append(f"  - `{f}`")

    if not parts:
        return "（空のメッセージ）"

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# リッチ応答チャット (旧 Tab 3)
# ---------------------------------------------------------------------------


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


# ---------------------------------------------------------------------------
# ストリーミングチャット (旧 Tab 4)
# ---------------------------------------------------------------------------

_DUMMY_RESPONSES = [
    "こんにちは！これはストリーミングのデモです。",
    "Gradio 6 では `yield` を使ってテキストを少しずつ返せます。",
    "ストリーミングにより、長い応答でもリアルタイムに表示されます。",
    "実際の LLM 応答もこの仕組みで逐次表示できます。",
]


def _stream_chat(message: str, history: list) -> str:
    idx = len(history) % len(_DUMMY_RESPONSES)
    response = _DUMMY_RESPONSES[idx]

    accumulated = ""
    for char in response:
        accumulated += char
        time.sleep(0.04)
        yield accumulated


# ---------------------------------------------------------------------------
# build_tab - 3つのチャットデモをサブタブで統合
# ---------------------------------------------------------------------------


def build_tab() -> None:
    with gr.Tab("Tab 2: チャットショーケース"):
        gr.Markdown(
            """## Tab 2: チャットショーケース

マルチモーダル・リッチ応答・ストリーミングの 3 種類のチャットデモを統合したタブです。
各サブタブで Gradio 6 の異なるチャット機能を確認できます。
"""
        )

        with gr.Tabs():
            # --- サブタブ: マルチモーダル ---
            with gr.Tab("マルチモーダル"):
                gr.Markdown(
                    """### マルチモーダルチャット

使用コンポーネント: `gr.ChatInterface(multimodal=True)`

- テキストと画像・ファイルを同時に送信できます
- `message` 引数は `{"text": str, "files": list[str]}` の形式で渡されます
- このタブは ADK 非使用のエコーデモです
"""
                )
                gr.ChatInterface(
                    fn=_chat_multimodal,
                    multimodal=True,
                )

            # --- サブタブ: リッチ応答 ---
            with gr.Tab("リッチ応答"):
                gr.Markdown(
                    """### リッチ応答チャットボット

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

            # --- サブタブ: ストリーミング ---
            with gr.Tab("ストリーミング"):
                gr.Markdown(
                    """### ストリーミングチャット

使用コンポーネント: `gr.ChatInterface(type="messages")` + `yield`

- `fn` が `yield` でテキストを少しずつ返すとリアルタイム表示されます
- `type="messages"` で OpenAI 互換のメッセージ形式を使用
- このタブは ADK 非使用のダミーストリームデモです
"""
                )
                gr.ChatInterface(
                    fn=_stream_chat,
                    title="",
                    description="何かメッセージを送ると、文字が1文字ずつストリーミング表示されます。",
                )
