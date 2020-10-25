import os

class Conll:

    def __init__(self):
        self.path = os.path.join(os.getcwd(), "nkjp.conll")

    def get_path(self):
        return self.path


    @staticmethod
    def sentence_factory(path_to_file):
        file = open(path_to_file, "r", encoding="utf-8")
        lines = file.readlines()
        result = []
        for x in lines:
            result.append(x.split(' \"')[0])
        file.close()
        result = [x.replace('"', '') for x in result]
        print(result)

        array_of_sentences = []
        sentence = ""
        end_of_sentence = ['.', '?', '!']
        for token in result:
            if sentence == "" or token == ',' or token == ';' or token in end_of_sentence:
                sentence += token
            elif token != ',':
                sentence += " " + token

            if token in end_of_sentence:
                array_of_sentences.append(sentence)
                sentence = ""

        print(array_of_sentences)


handler = Conll()
handler.sentence_factory(handler.path)
