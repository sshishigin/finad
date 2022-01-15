from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware
from finadscript import FinAdWorker

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


class FinAdForm(BaseModel):
    plain_text: str


@app.post("/fin-ad-analyze")
async def upload_file(data: FinAdForm):
    worker = FinAdWorker()
    response = worker.work(data.plain_text)
    print(response)
    return {"response_text": response}
