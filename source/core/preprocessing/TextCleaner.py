from unidecode import unidecode
import contractions
import pandas as pd
import inflect
import string
import re


class TextCleaner:
    """ This preprocessing step doesn't need any grammar rules or even a frequency analysis,
    it’s purely text manipulation. """

    def __init__(self, numbers: str = 'remove', twitter: bool = False, reddit: bool = False):
        self.is_twitter = twitter
        self.is_reddit = reddit
        self.treat_numbers = numbers

    def standardize(self, data: pd.Series):
        df = data.copy()

        # Drop urls
        df = df.apply(self.drop_links)

        # Treat social media data
        if self.is_reddit:
            pass
        elif self.is_twitter:
            pass

        # Treat number converting to text or/and removing
        if self.treat_numbers == 'convert':
            df = df.apply(self.number_to_text)
        df = df.apply(self.remove_numbers)  # if convert mode drop the remain

        # Expand contractions
        df = df.apply(self.expand_contractions)

        # Remove punctuation
        df = df.apply(self.remove_punctuation)

        # Convert special characters
        df = df.apply(self.special_characters_to_ascii)

        # Normalizing case
        df = df.apply(self.to_lower)

        # Remove extra whitespaces
        df = df.apply(self.remove_whitespaces)

        return df

    @staticmethod
    def to_lower(sentence: str):
        return sentence.lower()

    @staticmethod
    def number_to_text(sentence):
        p = inflect.engine()

        numbers = re.finditer(r'\d+', sentence)
        for x in reversed([x for x in numbers]):
            number = sentence[x.start():x.end()]

            if number.isdigit():
                word = p.number_to_words(number)
                sentence = sentence[:x.start()] + word + sentence[x.end():]

        return sentence

    @staticmethod
    def remove_numbers(sentence):
        return re.sub(r'\d+', '', sentence)

    @staticmethod
    def remove_punctuation(sentence):
        translator = str.maketrans('', '', string.punctuation)
        return sentence.translate(translator)

    @staticmethod
    def remove_whitespaces(sentence):
        return " ".join(sentence.split())

    @staticmethod
    def expand_contractions(sentence):
        # https://stackoverflow.com/questions/19790188/expanding-english-language-contractions-in-python
        return contractions.fix(sentence)

    @staticmethod
    def special_characters_to_ascii(sentence):
        return unidecode(sentence)

    @staticmethod
    def drop_links(sentence):
        return re.sub(r"http\S+", "", sentence)

    @staticmethod
    def drop_mentions(sentence):
        # @ToDo
        return sentence
