from io import BytesIO


try:
    from PIL import Image, ImageEnhance
except ImportError:
    import Image
import pytesseract


class FinAdWorker:
    @staticmethod
    def work(file):
        img = BytesIO(file)
        data = Image.open(img)
        threshold = 40
        data.point(lambda p: 255 if p > threshold else 0)
        return pytesseract.image_to_string(data, "rus")
