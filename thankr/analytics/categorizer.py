from textblob.classifiers import NaiveBayesClassifier

training_set_loc = "thankr/analytics/categorizer_training.json"
with open(training_set_loc, 'r') as fp:
    cl = NaiveBayesClassifier(fp, format="json")

if not cl:
    raise Exception("Categorizer could not initiate classifer with training set", training_set_loc)

def categorize(text):
    if not text:
        return ""
    return cl.classify(text)
