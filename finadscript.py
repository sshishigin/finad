from fastapi import UploadFile

try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract


class FinAdWorker:

    @staticmethod
    def work(file: UploadFile):
        with file.read() as file:
            return pytesseract.image_to_string(file, "rus")
