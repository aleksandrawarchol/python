import os
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

class Txt:  # czy ta klasa coś robi, oprócz metody statycznej tokenize?
    def __init__(self):
        self.path = os.path.join(os.getcwd(), "nkjp.txt")

    def get_path(self):
        return self.path

    @staticmethod
    def tokenize(pathToFile):
        file = open(pathToFile, "r", encoding='utf-8')  # lepiej nie przesłaniać nazw wbudowanych
        text = file.read()
        file.close()
        tokenized_text = word_tokenize(text)
        print(tokenized_text)
        tokenized_text = sent_tokenize(text)
        print(tokenized_text)


handler = Txt()
handler.tokenize(handler.path)

