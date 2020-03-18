from nltk import word_tokenize
class CollectUtterance:
    def __init__(self, utterance):
        self.utterance = utterance

    def collect_utterance(self):
        return word_tokenize(self.utterance.lower())