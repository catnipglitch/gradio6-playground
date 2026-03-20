# Gradio 6.9 Playground

Gradio 6.9.x の新機能・コンポーネントを網羅的にショーケースする実用リファレンスアプリ。

## 特徴

- Gradio 6.9 の主要機能を 12 タブ＋グローバル Sidebar で体験できる
- Google ADK (Agent Development Kit) による AI チャット機能
- テーマ・レイアウト・イベントシステムなど v6 新機能のデモ

## タブ構成

| # | タブ名 | 主なコンポーネント |
|---|--------|--------------------|
| — | Sidebar（グローバル） | `gr.Sidebar` — アプリ情報・バージョン表示 |
| 1 | AI チャット (ADK) | `gr.ChatInterface` + Google ADK |
| 2 | チャットショーケース | マルチモーダル / リッチ応答 / ストリーミング（サブタブ） |
| 3 | テキスト・数値入力 | `gr.Textbox` / `gr.Number` / `gr.Slider` / `gr.Code` |
| 4 | 選択・カラー入力 | `gr.Checkbox` / `gr.Radio` / `gr.Dropdown(multiselect)` / `gr.ColorPicker` |
| 5 | メディア入出力 | `gr.Image` / `gr.Audio` / `gr.Video` / `gr.Gallery` / `gr.AnnotatedImage` / `gr.DownloadButton` |
| 6 | 画像エディタ | `gr.ImageEditor` / `gr.Brush` / `gr.Eraser` |
| 7 | データ表示・出力 | `gr.Dataframe` / `gr.Label` / `gr.JSON` / `gr.Plot` / `gr.HTML` / `gr.ParamViewer` |
| 8 | レイアウト・構造 | `gr.Sidebar` / `gr.Accordion` / `gr.Group` / `render` · `unrender` |
| 9 | イベント・タイマー・状態 | `gr.Timer` / `.success()` · `.failure()` / `gr.on()` / `gr.State` |
| 10 | v6 新コンポーネント | `gr.FileExplorer` / `gr.DownloadButton` / `gr.ParamViewer` / `gr.AnnotatedImage` |
| 11 | テーマ・スタイリング | プリセットテーマ一覧 / プレビュー / CSS カスタマイズ |
| 12 | APIキー設定 | Gemini APIキー入力・認証テスト |

## セットアップ

### 前提条件

- Python 3.11+
- [astral uv](https://docs.astral.sh/uv/)

### インストール・起動

```bash
uv sync
uv run python main.py
```

ブラウザで `http://localhost:7860` を開いてください。

### 環境変数

AI チャット（Tab 1）を使用する場合は Gemini API キーが必要です。

```bash
cp .env.example .env
# .env に GEMINI_API_KEY を設定
```

または Tab 12 からブラウザ上でキーを入力できます（セッション限定）。

## 技術スタック

| 項目 | 仕様 |
|------|------|
| UI フレームワーク | Gradio >= 6.9 |
| AI SDK | Google ADK (Agent Development Kit) |
| パッケージ管理 | astral uv |
| ホスティング | GCP Cloud Run |

## ディレクトリ構成

```
gradio6-playground/
├── main.py                        # エントリーポイント
├── tabs/
│   ├── adk_utils.py               # ADK ユーティリティ
│   ├── tab01_chat.py              # Tab 1: AI チャット
│   ├── tab02_chat_showcase.py     # Tab 2: チャットショーケース
│   ├── tab03_text_inputs.py       # Tab 3: テキスト・数値入力
│   ├── tab04_selection.py         # Tab 4: 選択・カラー入力
│   ├── tab05_media.py             # Tab 5: メディア入出力
│   ├── tab06_image_editor.py      # Tab 6: 画像エディタ
│   ├── tab07_data_outputs.py      # Tab 7: データ表示・出力
│   ├── tab08_layout.py            # Tab 8: レイアウト・構造
│   ├── tab09_events_timer.py      # Tab 9: イベント・タイマー・状態
│   ├── tab10_new_v6.py            # Tab 10: v6 新コンポーネント
│   ├── tab11_theming.py           # Tab 11: テーマ・スタイリング
│   └── tab12_apikey.py            # Tab 12: APIキー設定
├── pyproject.toml
├── PRD.md                         # プロダクト要件定義
└── CLAUDE.md                      # AI アシスタント向け指示
```

## ライセンス

Apache License 2.0 — 詳細は [LICENSE](LICENSE) を参照してください。
