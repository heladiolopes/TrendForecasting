from nltk.corpus import stopwords
import pandas as pd


class StopWords:
    def __init__(self, lang='english'):
        # Get stopwords list for given language
        self.stopwords = set(stopwords.words(lang))

    def remove(self, data: pd.Series):
        return data.apply(self.__remove_stopwords)

    def __remove_stopwords(self, sentence: str):
        # Split the text in a list of words
        words = sentence.split(' ')

        # Filter the text, removing the stopwords
        words_filtered = [w for w in words if w not in self.stopwords]

        # Return filtered words as a text
        text_filtered = ' '.join(words_filtered)

        return text_filtered
