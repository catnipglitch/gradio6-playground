# Gradio 6 Playground

Gradio 6 の実験リポジトリ

## 技術スタック

- Python 3.11 固定
- パッケージ管理: astral uv
- AI: Google ADK (Agent Development Kit)

## アプリ構成

10個のタブを持ち、タブごとに異なる機能を実装する。

| タブ | 機能 |
|------|------|
| Tab 1 | チャットテスト |
| Tab 2〜9 | （未定） |
| Tab 10 | APIキー入力・認証テスト |

## APIキー管理

- **ローカル開発**: `.env` から Gemini APIキーを読み込む
- **Cloud Run**: シークレットマネージャー、またはセッション限定のキーを利用
- **ユーザー入力**: Tab 10 で受付

## デプロイ

- GCP Cloud Run へデプロイ
- GitHub からの自動デプロイ

## 開発方針

- GitHub Issue ベースで進行



## 追加要件
 gradio 6.5.x
 