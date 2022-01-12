from fastapi import FastAPI, UploadFile
from finadscript import FinAdWorker
app = FastAPI()


@app.post("/fin-ad-analyze")
async def root(file: UploadFile):
    picture_text = FinAdWorker.work()
    print(picture_text)
    return {"picture_text": picture_text}
