from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from sentiment_model import analyze_sentiment

app = FastAPI()

# Настройка шаблонов
templates = Jinja2Templates(directory="static")


class TextInput(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/analyze")
async def analyze_text(input: TextInput):
    sentiment = analyze_sentiment(input.text)
    return {"label": sentiment['label'], "score": sentiment['score']}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8080)
