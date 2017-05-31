from src.NegativeSentenceCreator import *

from src.GoogleResultsGetter import *


def probability_of_sentence(sentence):
    gs = GoogleResultsGetter("AIzaSyCZ9HvClGcCYqVxT9SruazjoHb9xNewuOM", "008201436329454125027:r1b12zwr7ko")
    try:
        true_score = gs.number_of_google_searches(sentence)
        negation = get_negative(sentence)
        false_score = gs.number_of_google_searches(negation)
        print(sentence)
        print("vs")
        print(negation)
        print("----------------------------")
        score_true = round(true_score / (true_score + false_score) * 100, 2)
        score_false = round(100.0 - score_true, 2)
        if score_true > 50:
            return True, score_true, score_false
        else:
            return False, score_true, score_false
    except urllib.error.URLError:
        print("Connection problems")
        return ""
    except ValueError:
        print("Wrong result")
        return ""


question = "Pope is dead"
answer, percents_true, percents_false = probability_of_sentence(question)

if not (answer == ""):
    print("Sentence : " + question)
    print("True  => " + str(percents_true) + "%")
    print("False => " + str(percents_false) + "%")
    print("Final answer => " + str(answer))
else:
    print("Error")
