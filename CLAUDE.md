# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

Gradio 6 + Google ADK による10タブ構成の実験的 Web アプリ。詳細は `PRD.md` を参照。
ユーザー要望は `FEATURES.md`、AI 向け要件定義は `PRD.md` に記載。

## 技術スタック

- Python 3.11（`.python-version` で固定）
- パッケージ管理: astral uv
- UI: Gradio 6
- AI: Google ADK (Gemini)
- デプロイ: GCP Cloud Run（GitHub からの自動デプロイ）

## リポジトリ

- GitHub: <https://github.com/catnipglitch/gradio6-playground>
- SSH: `git@github.com:catnipglitch/gradio6-playground.git`

## コマンド

```bash
# 依存パッケージインストール
uv sync

# アプリ起動
uv run python main.py

# パッケージ追加
uv add <package-name>
```

## アーキテクチャ

- エントリーポイント: `main.py`（Gradio Blocks 定義）
- 各タブの実装: `tabs/` ディレクトリに `tab01_chat.py`, `tab10_apikey.py` 等のファイルで分離
- APIキー: 環境変数 `GEMINI_API_KEY`（`.env` またはSecret Manager）、Tab 10 のユーザー入力（セッション限定）の2系統。ユーザー入力を優先。

## 開発ルール

- 開発は GitHub Issue ベース。Issue → ブランチ → PR で進行。
- Gradio 起動時は `server_name="0.0.0.0"`, `server_port=int(os.environ.get("PORT", 7860))` を指定。
- APIキーをログ出力・永続化しない。
- 日本語でコミュニケーションする。
