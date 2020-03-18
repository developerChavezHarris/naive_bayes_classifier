from text_classifier.classifier import Classification
from utterance.collect_utterance import CollectUtterance


classification_data_json_file = 'classification_data.json'

def classify_utterance():
    # Collect utterance
    utterance = CollectUtterance(utterance=input("Enter an utterance to classify : ")).collect_utterance()
    utterance = ' '.join(utterance)


    # Classify utterance
    file = classification_data_json_file
    intent = Classification(utterance, file).classify_intent()

    print('Intent ----> ' + intent)
    print('Utterance ----> ' + utterance)


while True:
    classify_utterance()
    exit = input("Type 'quit' to exit or press enter key to continue classifying: ")
    if exit == 'quit':
        break

