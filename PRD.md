# PRD: Gradio 6 Playground

## リポジトリ

- GitHub: <https://github.com/catnipglitch/gradio6-playground>
- SSH: `git@github.com:catnipglitch/gradio6-playground.git`

## 概要

Gradio 6 の UI コンポーネントを網羅的に試せる見本帳アプリ。
チャットの複数パターン・2D画像編集・各種入出力コンポーネントを実装し、次のアプリ開発の UI リファレンスとして活用する。
Google ADK (Agent Development Kit) を使った AI 機能は Tab 1 のみで使用。Tab 2〜9 は Gradio UI の展示に専念する。

## 技術要件

| 項目 | 仕様 |
|------|------|
| 言語 | Python 3.11（`.python-version` で固定済み） |
| パッケージ管理 | astral uv |
| UI フレームワーク | Gradio 6 |
| AI SDK | Google ADK (Agent Development Kit)（Tab 1 のみ） |
| ホスティング | GCP Cloud Run |
| CI/CD | GitHub → Cloud Run 自動デプロイ |

## 依存パッケージ（想定）

- `gradio` >= 6.x
- `google-adk`
- `python-dotenv`（ローカル開発用）
- `matplotlib`（Tab 9 のグラフ描画用）

> pyproject.toml の `dependencies` に追加すること。

## アプリ構成

エントリーポイント: `main.py`

アプリは単一の Gradio Blocks で構成し、10 個の `gr.Tab` を持つ。

```
gr.Blocks
├── Tab 1:  チャット（ADK）       ← ChatInterface + Google ADK
├── Tab 2:  チャット Multimodal   ← ChatInterface(multimodal=True)
├── Tab 3:  チャット リッチ応答   ← Chatbot(type="messages") 手動制御
├── Tab 4:  チャット Streaming    ← ChatInterface(type="messages") + yield
├── Tab 5:  テキスト・数値・コード ← Textbox / Number / Code / Slider
├── Tab 6:  選択系               ← Checkbox / Radio / Dropdown / DateTime / ColorPicker
├── Tab 7:  メディア              ← Image / Audio / Video / File / Gallery / ImageSlider
├── Tab 8:  ImageEditor           ← 2D編集（ブラシ・消しゴム・クロップ・Slider連携）
├── Tab 9:  出力・レイアウト      ← Plot / Label / JSON / Accordion / Sidebar / Group
└── Tab 10: APIキー設定           ← Gemini APIキー入力・検証
```

## 機能仕様

### Tab 1: チャット（ADK）

- Google ADK を使用したチャットインターフェイス
- `gr.ChatInterface` を使用
- Gemini モデルとの対話が可能であること

### Tab 2: チャット Multimodal（Issue #9）

- `gr.ChatInterface(multimodal=True)` を使用
- 入力が `MultimodalTextbox`（テキスト＋ファイル添付）になる
- ADK 不使用。受け取ったファイル数・テキストをエコー返答するシンプル実装
- Gradio 6 の `message = {"text": str, "files": list[str]}` 形式を明示

### Tab 3: チャット リッチ応答（Issue #10）

- `gr.Chatbot(type="messages")` — Gradio 6 新メッセージ形式
- `gr.Textbox` + `gr.Button` で手動送受信制御
- ADK 不使用。キーワードに応じて以下のデモ応答を返す
  - 「画像」→ `content: gr.Image()`
  - 「グラフ」→ `content: gr.Plot()` (matplotlib)
  - 「HTML」→ `content: gr.HTML()`
  - その他 → 通常のテキスト返答
- 応答の中に画像・グラフ・HTML を埋め込んで表示できることを確認

### Tab 4: チャット Streaming（Issue #11）

- `gr.ChatInterface(type="messages")` — Gradio 6 新メッセージ形式
- `history` が `[{"role": "user"/"assistant", "content": str}]` 形式になる
- `yield` でチャンク単位ストリーミング返答
- ADK 不使用。固定テキストをチャンク分割して yield するシンプル実装

### Tab 5: テキスト・数値・コード入力（Issue #12）

対象コンポーネント:
- `gr.Textbox`（1行・複数行・パスワード）
- `gr.Number`
- `gr.Code`（シンタックスハイライト付きコードエディター、言語切替）
- `gr.Slider`（min/max/step/デフォルト値）

仕様:
- 各コンポーネントに入力し「送信」ボタンを押すと値を `gr.JSON` に出力
- タブ冒頭に使用コンポーネント名を `gr.Markdown` で一覧表示

### Tab 6: 選択系コンポーネント（Issue #13）

対象コンポーネント:
- `gr.Checkbox`
- `gr.CheckboxGroup`（複数選択）
- `gr.Radio`
- `gr.Dropdown`（単選択・多選択 `multiselect=True`）
- `gr.DateTime`
- `gr.ColorPicker`

仕様:
- 「送信」ボタンで値をまとめて `gr.JSON` に出力
- タブ冒頭に使用コンポーネント名を `gr.Markdown` で一覧表示

### Tab 7: メディアコンポーネント（Issue #14）

対象コンポーネント:
- `gr.Image`（アップロード・Webcam 対応）
- `gr.Audio`（アップロード・マイク対応）
- `gr.Video`
- `gr.File`（単一・複数）
- `gr.Gallery`（複数画像表示）
- `gr.ImageSlider`（2枚の画像を比較スライド）

仕様:
- 各コンポーネントを `gr.Row` / `gr.Column` で整理して配置
- 入力→出力の echo パスを設定

### Tab 8: ImageEditor 2D編集（Issue #15）

対象コンポーネント:
- `gr.ImageEditor`
  - `canvas_size`（Gradio 6 で `crop_size` から変更）
  - `gr.Brush`（色・サイズ・不透明度）
  - `gr.Eraser`（サイズ）
  - Crop ツール
  - レイヤー管理
- `gr.Slider`（ブラシサイズ・不透明度のリアルタイム連携）
- `gr.ColorPicker`（ブラシ色選択）
- `gr.Image`（出力: composite 画像）

仕様:
- Slider で `brush_size` / `opacity` を変更 →「適用」ボタンで ImageEditor 設定を更新
- 「書き出し」ボタンで `composite` を `gr.Image` に出力
- `layers` の枚数を `gr.Markdown` で表示

### Tab 9: 出力・レイアウト（Issue #16）

対象コンポーネント（出力系）:
- `gr.Label`（分類結果バー付き）
- `gr.HighlightedText`（スパンハイライト）
- `gr.JSON`（ツリー表示）
- `gr.Plot`（matplotlib グラフ）
- `gr.HTML`

対象コンポーネント（レイアウト系）:
- `gr.Accordion`（折りたたみパネル）
- `gr.Sidebar`（**Gradio 6 新機能**: 左サイドバー、開閉可能）
- `gr.Group`
- `gr.Row` / `gr.Column`

仕様:
- `gr.Sidebar` にコントロールパネルを配置
- `gr.Accordion` の開閉デモ
- ボタンクリックで各出力コンポーネントにサンプルデータを表示

### Tab 10: APIキー設定

- Gemini APIキーの入力フォーム
- 入力されたキーの認証テスト（API 呼び出しで有効性を検証）
- 認証結果（成功/失敗）の表示

## Gradio 6 で注意すべき変更点（Gradio 5 との差分）

| 項目 | Gradio 5 | Gradio 6 |
|------|----------|----------|
| Chatbot メッセージ形式 | タプル `(user, assistant)` | dict `{"role": ..., "content": ...}` |
| ChatInterface type | なし | `type="messages"` オプション追加 |
| ImageEditor キャンバスサイズ | `crop_size` | `canvas_size` |
| サイドバー | なし | `gr.Sidebar` 追加 |

## APIキー管理

### 環境ごとの挙動

| 環境 | キー取得方法 | 詳細 |
|------|-------------|------|
| ローカル開発 | `.env` ファイル | `GEMINI_API_KEY` 環境変数として読み込み |
| Cloud Run | GCP Secret Manager | 環境変数としてマウント |
| ユーザー入力 | Tab 10 | セッション単位で有効。サーバーに永続化しない |

### 優先順位

1. Tab 10 でユーザーが入力したキー（セッション限定）
2. 環境変数 `GEMINI_API_KEY`（`.env` または Secret Manager 由来）

### セキュリティ要件

- APIキーはサーバーサイドのログに出力しない
- ユーザー入力のキーはセッション（Gradio State）に保持し、永続化しない
- `.env` は `.gitignore` に含まれている（確認済み）

## デプロイ

### Cloud Run 構成

- GitHub リポジトリからの自動デプロイ（Cloud Build または GitHub Actions）
- Dockerfile または `Procfile` を用意する
- ポート: Cloud Run のデフォルト（`PORT` 環境変数を参照）

### 起動コマンド（想定）

```bash
uv run python main.py
```

> Gradio アプリは `server_name="0.0.0.0"` かつ `server_port=int(os.environ.get("PORT", 7860))` で起動すること。

## ディレクトリ構成

```
gradio6-playground/
├── main.py                    # エントリーポイント・Gradio Blocks 定義
├── tabs/
│   ├── __init__.py
│   ├── adk_utils.py           # ADK ユーティリティ（Tab 1 用）
│   ├── tab01_chat.py          # Tab 1: チャット（ADK）
│   ├── tab02_chat_multimodal.py  # Tab 2: チャット Multimodal
│   ├── tab03_chat_rich.py     # Tab 3: チャット リッチ応答
│   ├── tab04_chat_streaming.py   # Tab 4: チャット Streaming
│   ├── tab05_text_inputs.py   # Tab 5: テキスト・数値・コード入力
│   ├── tab06_selection.py     # Tab 6: 選択系
│   ├── tab07_media.py         # Tab 7: メディア
│   ├── tab08_image_editor.py  # Tab 8: ImageEditor 2D編集
│   ├── tab09_outputs_layout.py   # Tab 9: 出力・レイアウト
│   └── tab10_apikey.py        # Tab 10: APIキー設定
├── pyproject.toml
├── .python-version
├── .env.example               # 環境変数テンプレート
├── Dockerfile
├── FEATURES.md                # ユーザー要望書
├── PRD.md                     # 本ドキュメント
└── README.md
```

## 開発方針

- GitHub Issue ベースで機能追加・バグ修正を管理
- 各タブの実装は個別の Issue → ブランチ → PR で進行
- Epic: #8 以下の子 Issue (#9〜#16) が Tab 2〜9 に対応
- FEATURES.md はユーザーの要望メモ、PRD.md は AI 向けの要件定義として使い分ける
- Tab 2〜9 は ADK 不使用。Gradio UI の動作確認に専念する
- 各タブ冒頭に `gr.Markdown` で使用コンポーネント一覧を表示すること
