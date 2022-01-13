from fastapi import FastAPI, UploadFile, File
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


@app.post("/fin-ad-analyze")
async def upload_file(file: UploadFile = File(...)):
    file_to_process = await file.read()
    picture_text = FinAdWorker.work(file_to_process)
    print(picture_text)
    return {"picture_text": picture_text}
