from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")

def translate(text: str, src_lang: str, tgt_lang: str) -> str:
    try:
        tokenizer.src_lang = src_lang
        encoded = tokenizer(text, return_tensors="pt")
        tgt_token_id = tokenizer.lang_code_to_id.get(tgt_lang)
        if tgt_token_id is None:
            return "[Translation Error] Unsupported target language code."
        generated = model.generate(**encoded, forced_bos_token_id=tgt_token_id)
        result = tokenizer.batch_decode(generated, skip_special_tokens=True)
        return result[0]
    except Exception as e:
        return f"[Translation Error] {str(e)}"
