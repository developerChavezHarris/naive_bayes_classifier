from textblob.classifiers import NaiveBayesClassifier
class Classification:
    def __init__(self, utterance, file):
        self.utterance = utterance
        self.file = file

    def classify_intent(self):
        with open(self.file, 'r') as fp:
            cl = NaiveBayesClassifier(fp, format='json')
        intent = cl.classify(self.utterance)
        return intent