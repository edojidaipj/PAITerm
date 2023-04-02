# PAITerm

OpenAIのAPIに接続し、質問を送信して回答を取得します。

回答は標準出力に表示されるか、指定されたディレクトリにMarkdown形式で保存されます。

## **必要なパッケージ**

- Python 3.7+
- httpx
- asyncio

## **使用方法**

1. 必要なパッケージをインストールします。

```
pip install httpx asyncio
```

環境変数**`OPENAI_API_KEY`**にOpenAIのAPIキーを設定します。

```bash
echo 'export OPENAI_API_KEY="ここにAPIキーをペースト"' >> ~/.zshrc
```

エイリアスを追加します。

```bash
echo 'alias 任意のエイリアス="python /path/to/PAITerm/main.py"' >> ~/.zshrc
```

`.zshrc` ファイルを再読み込み。

```bash
source ~/.zshrc
```

## 使用例（エイリアスとして「ai」を設定）

```bash
% ai 'laravel10で認証機能を追加する方法をハンズオン形式で教えて下さい'
```

プログラムは回答を標準出力に表示します。

### オプション

**`-markdown`**または**`m`**オプションを使って、回答を指定されたディレクトリにMarkdown形式で保存できます。

デフォルトのディレクトリ名は "ChatGPT" です。

```bash
% ai 'laravel10で認証機能を追加する方法をハンズオン形式で教えて下さい' --markdown
```
