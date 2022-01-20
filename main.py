from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from finadscript import FinAdWorker
from keywords import keywords

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

red_warning = "<p class='font-italic'> Обратите, пожалуйста, внимание на то, что запрещено использование слов и фраз, " \
              "выделенных <span " \
              "style='color: red'> красным </span> цветом, если данные формулировки ничем не подтверждаются. Замените " \
              "или удалите слова и фразы, выделенные красным, во избежание привлечения к административной " \
              "ответственности.</p> "

orange_warning = "<p class='font-italic'> Рекомендуется пересмотреть использование слов и фраз, выделенных <span style='color: orange'> " \
                 "оранжевым </span> цветом, во избежание штрафа за необоснованное использование сравнительной " \
                 "степени. </p> "


class FinAdForm(BaseModel):
    plain_text: str


@app.post("/fin-ad-analyze")
async def upload_file(data: FinAdForm):
    worker = FinAdWorker(keywords)
    response, colors = worker.work(data.plain_text)
    warnings = []
    if "red" in colors:
        warnings.append(red_warning)
    if "orange" in colors:
        warnings.append(orange_warning)
    return {"response_text": response, "warnings": warnings}
