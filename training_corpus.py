from corpus import Corpus
from collections import defaultdict
import os


class TrainingCorpus(Corpus):
    def __init__(self, corpus_path):
        self.corpus_path = corpus_path
        self.all_words = defaultdict(lambda: [0, 0])

        self.spam_count = 0
        self.ham_count = 0

    def set_spam_or_ham(self, tag):
        spam_tag = tag == "SPAM"
        ok_tag = tag == "OK"
        truth_path = os.path.join(self.corpus_path, "!truth.txt")
        with open(truth_path, 'r', encoding="utf-8") as truth:
            for line in truth:
                words = line.split()
                if spam_tag:
                    self.spam_count += 1 if words[1] == "SPAM" else 0
                    yield words[0], super().readfile(os.path.join(self.corpus_path, words[0]))
                else:
                    self.ham_count += 1 if words[1] == "OK" else 0
                    yield words[0], super().readfile(os.path.join(self.corpus_path, words[0]))


    def count_all_words(self):
        # 0 - SPAM, 1 - OK
        counts = defaultdict(lambda:[0, 0])
        self.parse_words("SPAM", 0, counts)
        self.parse_words("OK", 1, counts)
        probabilities = self.set_probability(counts)
        return probabilities


    def parse_words(self, tag, tag_index, counts):
        for name, content in self.set_spam_or_ham(tag):
            for word in content:
                counts[word][tag_index] += 1


    def set_probability(self, counts):
        min_k = 1
        all_probabilities = set()
        for word, frequency in counts.items():
            spam_probability = (frequency[0] + min_k) / (self.spam_count + 2*min_k)
            ham_probability = (frequency[1] + min_k) / (self.ham_count + 2*min_k)
            all_probabilities.add(word, spam_probability, ham_probability)

        return all_probabilities
  