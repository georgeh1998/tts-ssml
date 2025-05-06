from google.cloud import texttospeech
import xml.etree.ElementTree as ET
import os

def read_ssml_file(file_path):
    """SSMLファイルを読み込む"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def text_to_speech(ssml_text, output_file):
    """Google Cloud Text-to-Speech APIを使用して音声を生成"""
    # クライアントの初期化
    client = texttospeech.TextToSpeechClient()

    # SSMLテキストの設定
    synthesis_input = texttospeech.SynthesisInput(ssml=ssml_text)

    # 音声設定
    voice = texttospeech.VoiceSelectionParams(
        language_code="ja-JP",
        name="ja-JP-Neural2-A",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    # 音声ファイルの設定
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # 音声合成の実行
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    # 音声ファイルの保存
    with open(output_file, "wb") as out:
        out.write(response.audio_content)
        print(f"音声ファイルが保存されました: {output_file}")

def main():
    # 環境変数の設定
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "test.json"

    # SSMLファイルの読み込み
    ssml_text = read_ssml_file("upload.xml")
    
    # 音声ファイルの生成
    text_to_speech(ssml_text, "output.mp3")

if __name__ == "__main__":
    main() 