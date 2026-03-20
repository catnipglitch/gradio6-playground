from __future__ import annotations

import time

import gradio as gr


def _step1(text: str) -> str:
    if not text:
        raise ValueError("入力が空です")
    return f"Step 1: {text}"


def _step2(text: str) -> str:
    return f"Step 2: {text} → 処理完了"


def _on_error() -> str:
    return "エラーが発生しました"


def build_tab() -> None:
    with gr.Tab("Tab 9: イベント・タイマー・状態"):
        gr.Markdown(
            """## Tab 9: イベント・タイマー・状態

`gr.Timer` / イベントチェーン (`.then()` / `.success()`) / `gr.on()` / `gr.State` の動作デモです。
"""
        )

        # ── Section 1: gr.Timer ──────────────────────────────────
        gr.Markdown(
            """### gr.Timer — リアルタイムカウンター / クロック

`gr.Timer(1)` で 1 秒ごとにコールバックを実行し、タイムスタンプを更新します。
カウンターは `every=1` を使ったスタート / ストップ制御のデモです。
"""
        )

        with gr.Row():
            with gr.Column():
                gr.Markdown("#### タイムスタンプ（自動更新）")
                timer = gr.Timer(1)
                timestamp = gr.Number(label="現在のタイムスタンプ")
                timer.tick(lambda: round(time.time()), outputs=timestamp)

            with gr.Column():
                gr.Markdown("#### カウンター（手動制御）")
                counter = gr.Number(value=0, label="カウンター")
                counter_timer = gr.Timer(1, active=False)
                counter_timer.tick(lambda x: x + 1, counter, counter)
                with gr.Row():
                    start_btn = gr.Button("開始")
                    stop_btn = gr.Button("停止")
                start_btn.click(lambda: gr.Timer(active=True), None, counter_timer)
                stop_btn.click(lambda: gr.Timer(active=False), None, counter_timer)

        # ── Section 2: Event chain ───────────────────────────────
        gr.Markdown(
            """### イベントチェーン — `.success()` / `.failure()`

`.click()` → `.success()` → 次のステップと連鎖します。
空文字列を送信すると `ValueError` が発生し、`.failure()` 側のハンドラが呼ばれます。
"""
        )

        with gr.Row():
            input_text = gr.Textbox(label="入力")
        with gr.Row():
            output1 = gr.Textbox(label="Step 1 結果")
            output2 = gr.Textbox(label="Step 2 結果")
            error_output = gr.Textbox(label="エラー")

        chain_btn = gr.Button("実行")
        chain_btn.click(_step1, input_text, output1).success(
            _step2, output1, output2
        ).failure(_on_error, outputs=error_output)

        # ── Section 3: gr.on() ───────────────────────────────────
        gr.Markdown(
            """### gr.on() — 複数トリガー → 単一ハンドラ

`gr.on()` を使うと、複数コンポーネントの変更イベントをまとめて 1 つのハンドラで処理できます。
どちらのテキストボックスを編集しても結合結果がリアルタイムに更新されます。
"""
        )

        with gr.Row():
            text1 = gr.Textbox(label="入力A")
            text2 = gr.Textbox(label="入力B")
        combined_output = gr.Textbox(label="結合結果")

        gr.on(
            triggers=[text1.change, text2.change],
            fn=lambda a, b: f"{a} + {b}",
            inputs=[text1, text2],
            outputs=combined_output,
        )

        # ── Section 4: gr.State ──────────────────────────────────
        gr.Markdown(
            """### gr.State — コンポーネント間の状態共有

`gr.State` はブラウザセッションごとに値を保持する非表示コンポーネントです。
ボタン操作で状態値をインクリメント / デクリメント / リセットできます。
"""
        )

        state = gr.State(value=0)
        display = gr.Number(label="状態値")
        with gr.Row():
            inc_btn = gr.Button("+1")
            dec_btn = gr.Button("-1")
            reset_btn = gr.Button("リセット")

        inc_btn.click(lambda s: (s + 1, s + 1), state, [state, display])
        dec_btn.click(lambda s: (s - 1, s - 1), state, [state, display])
        reset_btn.click(lambda: (0, 0), None, [state, display])
