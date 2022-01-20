import re
from copy import copy


class FinAdWorker:
    def __init__(self, keywords):
        self.keywords = keywords
        self.template_components = {"start_tag": "<p>", "end_tag": "</p>"}

    def work(self, text: str):
        processed_text = copy(text)
        colors = []
        for color, words in self.keywords.items():
            for word in words:
                matches = re.findall(word, text)
                for match in matches:
                    processed_text = processed_text.replace(match, self.color_word(match, color))
                    colors.append(color)

        processed_text = (
            self.template_components["start_tag"]
            + processed_text
            + self.template_components["end_tag"]
        )
        print(processed_text)
        colors = set(colors)
        return processed_text, colors

    def color_word(self, word, color: str = "orange"):
        return f"<span style='color: {color}'>{word}</span>"
