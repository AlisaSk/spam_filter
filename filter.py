from corpus import Corpus
from training_corpus import TrainingCorpus
import os

class MyFilter:
    def init(self):
        self.positive = "SPAM"
        self.negative = "OK"
        self.flag_words = {}

    # здесь фильтр тренируется
    def train(self, corpus_path):
        corpus = Corpus(corpus_path)
        for email  in corpus.emails():
            if email[0] == "!truth.txt":
                pass
            

    # здесь возвращает файл !prediction
    def test(self, corpus_path):
        corpus = Corpus(corpus_path)
        my_file = open(os.path.join(corpus_path, "!prediction.txt"), "w+")
        for email  in corpus.emails():
            prediction = email[0] + " OK\n"
            my_file.write(prediction)
        my_file.close()

        return my_file