# PRD: Gradio 6.9 Playground

## リポジトリ

- GitHub: <https://github.com/catnipglitch/gradio6-playground>
- SSH: `git@github.com:catnipglitch/gradio6-playground.git`

## 概要

Gradio 6.9.x の新機能・変更点を網羅的にショーケースする実用リファレンスアプリ。
12タブ＋グローバル Sidebar 構成で、チャット・入出力・レイアウト・イベント・テーマなど Gradio 6 の機能を幅広くデモする。
Google ADK (Agent Development Kit) を使った AI 機能は Tab 1 のみで使用。Tab 2〜11 は Gradio UI の展示に専念する。

## 技術要件

| 項目 | 仕様 |
|------|------|
| 言語 | Python 3.11（`.python-version` で固定済み） |
| パッケージ管理 | astral uv |
| UI フレームワーク | Gradio >= 6.9 |
| AI SDK | Google ADK (Agent Development Kit)（Tab 1 のみ） |
| ホスティング | GCP Cloud Run |
| CI/CD | GitHub → Cloud Run 自動デプロイ |

## 依存パッケージ

- `gradio` >= 6.9
- `google-adk`
- `python-dotenv`（ローカル開発用）
- `matplotlib`（グラフ描画用）

## アプリ構成

エントリーポイント: `main.py`

アプリは単一の Gradio Blocks で構成し、グローバル Sidebar + 12 個の `gr.Tab` を持つ。

```
gr.Blocks(title="Gradio 6.9 Playground")
│
├── gr.Sidebar（グローバル）          ← アプリ情報・Gradio バージョン表示
│
├── Tab 1:  AI チャット (ADK)         ← ChatInterface + Google ADK
├── Tab 2:  チャットショーケース       ← マルチモーダル/リッチ応答/ストリーミング（サブタブ）
├── Tab 3:  テキスト・数値入力         ← Textbox / Number / Code / Slider
├── Tab 4:  選択・カラー入力           ← Checkbox / Radio / Dropdown(multiselect) / ColorPicker
├── Tab 5:  メディア入出力             ← Image / Audio / Video / File / Gallery / AnnotatedImage / DownloadButton
├── Tab 6:  画像エディタ               ← ImageEditor / Brush / Eraser / Slider連携
├── Tab 7:  データ表示・出力           ← Label / HighlightedText / JSON / Plot / Dataframe / HTML / ParamViewer
├── Tab 8:  レイアウト・構造           ← Sidebar / Row / Column / Accordion / Group / render・unrender
├── Tab 9:  イベント・タイマー・状態   ← Timer / イベントチェーン / gr.on() / State
├── Tab 10: v6 新コンポーネント        ← FileExplorer / DownloadButton / ParamViewer / AnnotatedImage
├── Tab 11: テーマ・スタイリング       ← プリセットテーマ一覧 / プレビュー / CSS カスタマイズ
└── Tab 12: APIキー設定               ← Gemini APIキー入力・検証
```

## 機能仕様

### Tab 1: AI チャット (ADK)

- Google ADK を使用したチャットインターフェイス
- `gr.ChatInterface` を使用
- Gemini モデルとの対話が可能であること

### Tab 2: チャットショーケース

- 旧 Tab 2-4 を統合し、3つのサブタブで構成
- **マルチモーダル**: `gr.ChatInterface(multimodal=True)` でテキスト＋ファイル送信
- **リッチ応答**: `gr.Chatbot(type="messages")` でテキスト/画像/グラフ/HTML の表示
- **ストリーミング**: `yield` による文字単位のストリーミング表示

### Tab 3: テキスト・数値入力

- `gr.Textbox`（複数行・パスワード）/ `gr.Number` / `gr.Slider` / `gr.Code`
- 各コンポーネントに入力し「確認」ボタンで値を表示

### Tab 4: 選択・カラー入力

- `gr.Checkbox` / `gr.CheckboxGroup` / `gr.Radio` / `gr.Dropdown` / `gr.Dropdown(multiselect=True)` / `gr.ColorPicker`
- 「確認」ボタンで選択値を表示

### Tab 5: メディア入出力

- `gr.Image` / `gr.Audio` / `gr.Video` / `gr.File` / `gr.Gallery`（既存）
- `gr.AnnotatedImage`（バウンディングボックス付き画像表示）
- `gr.DownloadButton`（ファイルダウンロード）

### Tab 6: 画像エディタ

- `gr.ImageEditor` + `gr.Brush` / `gr.Eraser`
- ブラシサイズの Slider 連携
- 「適用」ボタンで composite 画像を出力

### Tab 7: データ表示・出力

- `gr.Label`（分類スコア表示）/ `gr.HighlightedText`（スパンハイライト）
- `gr.JSON`（ツリー表示）/ `gr.Plot`（matplotlib）
- `gr.Dataframe`（テーブル表示）
- `gr.HTML`（カスタム HTML）/ `gr.ParamViewer`（パラメータ情報）

### Tab 8: レイアウト・構造

- `gr.Sidebar` — タブ内サイドバーデモ
- `gr.Row` / `gr.Column` — `scale` / `min_width` パラメータ
- `gr.Accordion` — ネスト対応の折りたたみパネル
- `gr.Group` — 視覚的グルーピング
- `.render()` / `.unrender()` — 動的コンポーネント再配置

### Tab 9: イベント・タイマー・状態

- `gr.Timer` — リアルタイムカウンター/クロック
- イベントチェーン — `.success()` / `.failure()` / `.then()`
- `gr.on()` — 複数トリガー → 単一ハンドラ
- `gr.State` — コンポーネント間の状態共有

### Tab 10: v6 新コンポーネント

- `gr.FileExplorer` — サーバーサイドファイルブラウザ
- `gr.DownloadButton` — ファイルダウンロード
- `gr.ParamViewer` — パラメータ情報表示
- `gr.AnnotatedImage` — アノテーション付き画像

### Tab 11: テーマ・スタイリング

- プリセットテーマ一覧（Default / Soft / Glass / Monochrome / Ocean / Citrus / Origin）
- テーマプレビュー用サンプルコンポーネント群
- テーマカスタマイズ方法の解説
- CSS カスタマイズデモ（`elem_id` / `elem_classes`）

### Tab 12: APIキー設定

- Gemini APIキーの入力フォーム
- 認証テスト（API 呼び出しで有効性を検証）
- 認証結果（成功/失敗）の表示

## Gradio 6 で注意すべき変更点（v5 との差分）

| 項目 | Gradio 5 | Gradio 6 |
|------|----------|----------|
| Chatbot メッセージ形式 | タプル `(user, assistant)` | dict `{"role": ..., "content": ...}` |
| ChatInterface type | なし | `type="messages"` オプション追加 |
| ImageEditor キャンバスサイズ | `crop_size` | `canvas_size` |
| サイドバー | なし | `gr.Sidebar` 追加 |
| タイマー | なし | `gr.Timer` 追加 |
| `gr.on()` | なし | 複数トリガーの統合 |
| Dataframe | `col_count` | `column_count`（v6.9 で変更） |
| Image ボタン | `show_download_button` 等 | `buttons=["download", ...]` |

## APIキー管理

### 環境ごとの挙動

| 環境 | キー取得方法 | 詳細 |
|------|-------------|------|
| ローカル開発 | `.env` ファイル | `GEMINI_API_KEY` 環境変数として読み込み |
| Cloud Run | GCP Secret Manager | 環境変数としてマウント |
| ユーザー入力 | Tab 12 | セッション単位で有効。サーバーに永続化しない |

### 優先順位

- Tab 12 でユーザーが入力したキー（セッション限定）
- 環境変数 `GEMINI_API_KEY`（`.env` または Secret Manager 由来）

### セキュリティ要件

- APIキーはサーバーサイドのログに出力しない
- ユーザー入力のキーはセッション（Gradio State）に保持し、永続化しない
- `.env` は `.gitignore` に含まれている（確認済み）

## デプロイ

### Cloud Run 構成

- GitHub リポジトリからの自動デプロイ（Cloud Build または GitHub Actions）
- Dockerfile または `Procfile` を用意する
- ポート: Cloud Run のデフォルト（`PORT` 環境変数を参照）

### 起動コマンド

```bash
uv run python main.py
```

> Gradio アプリは `server_name="0.0.0.0"` かつ `server_port=int(os.environ.get("PORT", 7860))` で起動すること。

## ディレクトリ構成

```
gradio6-playground/
├── main.py                        # エントリーポイント・Gradio Blocks 定義
├── tabs/
│   ├── __init__.py
│   ├── adk_utils.py               # ADK ユーティリティ（Tab 1 用）
│   ├── tab01_chat.py              # Tab 1: AI チャット (ADK)
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
├── .python-version
├── .env.example                   # 環境変数テンプレート
├── Dockerfile
├── PRD.md                         # 本ドキュメント（要件定義・開発ルール）
└── README.md
```

## コマンド

| 操作 | コマンド |
|------|---------|
| 依存パッケージインストール | `uv sync` |
| アプリ起動 | `uv run python main.py` |
| パッケージ追加 | `uv add <package-name>` |

## 開発ルール

- 開発は GitHub Issue ベース。Issue → ブランチ → PR で進行
- Gradio 起動時は `server_name="0.0.0.0"`, `server_port=int(os.environ.get("PORT", 7860))` を指定
- APIキーをログ出力・永続化しない
- 日本語でコミュニケーションする
- Gradio バージョン: 6.9.x を対象とする
- Tab 2〜11 は ADK 不使用。Gradio UI の動作確認に専念する
- 各タブ冒頭に `gr.Markdown` で使用コンポーネント一覧を表示すること
