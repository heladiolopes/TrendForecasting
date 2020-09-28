from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import pandas as pd
import nltk


class Lemmatization:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

    def sentence_to_lemma(self, sentence: str):
        # Split the text in a list of words
        words = sentence.split(' ')

        # Find the pos tagging for each tokens
        pos_tokens = nltk.pos_tag(words)

        # Apply lemmatization using pos tagg
        words_lemma = [self.lemmatizer.lemmatize(word, self.get_wordnet_pos(tag)) for word, tag in pos_tokens]

        # Return lemma words as a text
        text_lemma = ' '.join(words_lemma)

        return text_lemma

    def normalize(self, data: pd.Series):
        return data.apply(self.sentence_to_lemma)

    def get_wordnet_pos(self, treebank_tag):
        if treebank_tag.startswith('J'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return wordnet.NOUN
