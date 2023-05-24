import string
import re
from typing import List


class BasicTokenizer:
    """
    Basic text preprocessing. Use this class to preprocess text
    """

    def __init__(self):
        self.__cleaned_text = None

    @property
    def cleaned_text(self):
        if self.__cleaned_text is None:
            raise AttributeError("Text has not been cleaned")
        return self.__cleaned_text

    def tokenize(self, text: str) -> List[str]:
        cleaned_text = self._process_text(text)
        cleaned_text = " ".join(cleaned_text.split())
        self.__cleaned_text = cleaned_text
        return cleaned_text.split()

    def _process_text(self, text: str) -> str:
        """
        Runs basic text cleaning and splitting on a piece of text.
        """
        text = self._remove_html_tag(text)
        text = self._remove_punctuation(text)
        text = self._remove_non_english_alphabet(text)
        text = self._to_lowercase(text)
        return text

    @staticmethod
    def _remove_html_tag(text: str) -> str:
        return re.sub("<.*?>", " ", text)

    @staticmethod
    def _remove_punctuation(text: str) -> str:
        return text.translate(str.maketrans(' ', ' ', string.punctuation))

    @staticmethod
    def _remove_non_english_alphabet(text: str) -> str:
        return re.sub("[^a-zA-Z]", " ", text)

    @staticmethod
    def _to_lowercase(text: str) -> str:
        return text.lower()
