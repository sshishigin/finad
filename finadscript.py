import random
from copy import copy

keywords = [
    "лучший",
    "первый",
    "номер один",
    "самый",
    "только",
    "единственный",
    "самые низкие цены",
    "самое выгодное предложение",
]


class FinAdWorker:
    def __init__(self):
        self.template_components = {"start_tag": "<p>", "end_tag": "</p>"}

    def work(self, text: str):
        detected_keywords = self.find_keywords(text)
        print(detected_keywords)
        processed_text = copy(text)
        for word in detected_keywords:
            processed_text = processed_text.replace(word, self.color_word(word, random.choice(["red", "orange"])))
        processed_text = self.template_components["start_tag"] + processed_text + self.template_components["end_tag"]
        return processed_text

    def find_keywords(self, text: str):
        return [keyword for keyword in keywords if keyword in text.lower()]

    def color_word(self, word, color: str = "orange"):
        return f"<span style='color: {color}'>{word}</span>"
