import string
import re


class Text:
    """
    Basic text preprocessing. Use this class to preprocess text
    """

    def __init__(self, text: str):
        self.text = text

    @property
    def cleaned_text(self):
        output = self._remove_html()
        output = self._remove_punctuation(output)
        output = self._remove_non_english_alphabet(output)
        output = self._to_lowercase(output)
        return " ".join(output.split())

    def _remove_html(self) -> str:
        return re.sub("<.*?>", " ", self.text)

    def _remove_punctuation(self, text: str) -> str:
        return text.translate(str.maketrans(' ', ' ', string.punctuation))

    def _remove_non_english_alphabet(self, text: str) -> str:
        return re.sub("[^a-zA-Z]", " ", text)

    def _to_lowercase(self, text: str) -> str:
        return text.lower()

    
class BasicTokenizer:
    ...


# class Token(Text):
#     def __init__(self, text: str):
#         super().__init__(text)

#     @property
#     def tokenized_data(self):
#         stpw = set(stopwords.words("english"))
#         wtkn = self._tokenize(self.cleaned_text)
#         return [w for w in wtkn if not w in stpw]

#     @staticmethod
#     def _tokenize(text):
#         return word_tokenize(text)

    # @staticmethod
    # def get_tokens(workd):
    #     pass

    # def _remove_stopwords(self):
    #     pass

    # def _stemming(self):
    #     pass

    # def _lemmatization(self):
    #     pass
