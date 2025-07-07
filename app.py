from fastapi import FastAPI, Request
from model import translate

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Matre Translator Server is Running"}

@app.post("/translate")
async def do_translate(req: Request):
    try:
        data = await req.json()
        text = data.get("text")
        source = data.get("from")
        target = data.get("to")

        if not text or not source or not target:
            return {"error": "Missing 'text', 'from', or 'to' fields in request."}

        result = translate(text, source, target)
        return {"translated": result}
    except Exception as e:
        return {"error": str(e)}
