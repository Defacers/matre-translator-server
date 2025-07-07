# Matre Translator Server

Translator AI ringan berbasis FastAPI untuk hasil OCR dari komik/manga.

## Endpoint API

- POST /translate

Contoh Request:
```json
{
  "text": "こんにちは",
  "from": "jpn_Jpan",
  "to": "eng_Latn"
}
```

Contoh Response:
```json
{
  "translated": "Hello"
}
```

Bahasa yang Didukung

jpn_Jpan → Japanese

zho_Hans → Chinese Simplified

zho_Hant → Chinese Traditional

kor_Hang → Korean

eng_Latn → English

ind_Latn → Indonesian


> Lihat daftar lengkap:
https://huggingface.co/facebook/nllb-200-distilled-600M#languages
