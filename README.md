# TTS-SSML

Google Cloud Text-to-Speech APIを使用してSSMLファイルを音声に変換するツールです。

## 必要条件

- Python 3.8以上
- Google Cloud Platformのアカウント
- Google Cloud Text-to-Speech APIの有効化
- サービスアカウントの認証情報（JSONファイル）

## セットアップ

1. 必要なパッケージのインストール:
```bash
uv venv
uv pip install -e .
```

2. Google Cloud Platformの認証情報を設定:
   - `test.json`という名前でサービスアカウントの認証情報ファイルをプロジェクトのルートディレクトリに配置してください。

## 実行方法

1. SSMLファイルの準備:
   - `upload.xml`という名前でSSMLファイルをプロジェクトのルートディレクトリに配置してください。
   - SSMLファイルはUTF-8エンコーディングで保存してください。

2. スクリプトの実行:
```bash
python main.py
```

3. 出力:
   - 生成された音声ファイルは`output.mp3`として保存されます。

## SSMLファイルの例

```xml
<?xml version="1.0" encoding="UTF-8"?>
<speak>
  <voice name="ja-JP-Neural2-A">
    こんにちは、これはテストです。
  </voice>
</speak>
```

## 注意事項

- Google Cloud Platformの利用には料金が発生する場合があります。
- 音声の品質や利用可能な音声は、Google Cloud Text-to-Speech APIの仕様に依存します。 