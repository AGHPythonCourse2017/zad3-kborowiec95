from VerbsFinder import *

tense_verbs = ["am", "are", "is",
               "was", "were",
               "has", "have", "had",
               "will", "would", "do", "did"]


def find_verb(sentence):
    words = sentence.split(" ")
    for i in range(0, len(words)):
        if words[i] in tense_verbs:
            return words[i], i, words
    return "", "", words


def create_negative(index, words, negative_form):
    result = ""
    for i in range(0, index):
        result += (words[i] + " ")
    result += (negative_form + " ")
    for i in range(index + 1, len(words) - 1):
        result += (words[i] + " ")
    result += words[len(words) - 1]
    return result


def get_negative(sentence):
    # check all tenses apart from past and present simple :
    verb, index, words = find_verb(sentence)
    if verb != "":
        # creating sentence with 'not'
        return create_negative(index, words, words[index] + " not")

    # check past simple and present simple :
    verbs_finder = VerbsFinder()
    negative_verb, index, words = verbs_finder.get_negative_verb(sentence)
    if negative_verb != "":
        return create_negative(index, words, negative_verb)

    # verb haven't found :
    return ""
