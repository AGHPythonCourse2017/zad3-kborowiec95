from NegativeSentenceCreator import *

from TruthChecker.GoogleResultsGetter import *


def create_question(args):
    n = len(args)
    result = ""
    for i in range(1, n - 1):
        result += (str(args[i]) + " ")
    result += str(args[n - 1])
    return result


def probability_of_sentence(sentence):
    gs = GoogleResultsGetter("AIzaSyCZ9HvClGcCYqVxT9SruazjoHb9xNewuOM", "008201436329454125027:r1b12zwr7ko")
    try:
        true_score = gs.number_of_google_searches(sentence)
        vf = VerbsFinder()
        negation = get_negative_sentence(sentence, vf)
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
        return "", "", ""
    except ValueError:
        print("Wrong result")
        return "", "", ""


def run(question):
    answer, percents_true, percents_false = probability_of_sentence(question)
    if not (answer == ""):
        print("Sentence : " + question)
        print("True  => " + str(percents_true) + "%")
        print("False => " + str(percents_false) + "%")
        print("Final answer => " + str(answer))
    else:
        print("Error")
        exit(0)
