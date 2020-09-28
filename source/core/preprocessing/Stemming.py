from nltk.stem import PorterStemmer, LancasterStemmer
import pandas as pd


class Stemming:
    def __init__(self, algorithm: str = 'Porter'):
        self.type = algorithm.lower()
        self.stemmer = self.__get_selected_stemmer()

    def __get_selected_stemmer(self):
        if self.type == 'porter':
            return PorterStemmer()
        elif self.type == 'lancaster':
            return LancasterStemmer()

    def __sentence_to_stems(self, sentence: str):
        # Split the text in a list of words
        words = sentence.split(' ')

        # Apply lemmatizer algorithm in words
        words_stemmed = [self.stemmer.stem(w) for w in words]

        # Return stemmed words as a text
        text_stemmed = ' '.join(words_stemmed)

        return text_stemmed

    def normalize(self, data: pd.Series):
        return data.apply(self.__sentence_to_stems)

