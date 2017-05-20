from GoogleResultsGetter import *
from NegativeSentenceCreator import *


def probability_of_sentence(sentence):
    gs = google_searcher()
    try:
        true_score = gs.number_of_google_searches(sentence)
        print(sentence+" -> "+str(true_score))
        negative = get_negative(sentence)
        false_score = gs.number_of_google_searches(negative)
        print(negative+" -> "+str(false_score))
        score = true_score / (true_score + false_score) * 100
        if score > 50:
            return score, 1
        else:
            return score, 0
    except urllib.error.URLError:
        print("Connection problems")
        return "", ""
    except ValueError:
        print("Wrong result")
        return "", ""


print(probability_of_sentence("People like The Beatles"))
