from GoogleResultsGetter import *
from NegativeSentenceCreator import *


def probability_of_sentence(sentence):
    gs = google_searcher()
    try:
        true_score = gs.number_of_google_searches(sentence)
        negative = get_negative(sentence)
        false_score = gs.number_of_google_searches(negative)
        print(sentence)
        print("vs")
        print(negative)
        print("----------------------------")
        score = round(true_score / (true_score + false_score) * 100, 2)
        if score > 50:
            return True, score
        else:
            return False, round(100.0 - score, 2)
    except urllib.error.URLError:
        print("Connection problems")
        return "", ""
    except ValueError:
        print("Wrong result")
        return "", ""


sentence = "Cracow is in Poland"
answer, percents = probability_of_sentence(sentence)
print("Sentence : " + sentence + " => " + str(answer) + " for : " + str(percents) + "%")
