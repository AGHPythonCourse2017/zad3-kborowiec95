from TruthChecker.VerbsFinder import *


def get_negative_verb(full_sentence, verbs_finder):
    words = full_sentence.split(" ")
    verb, index = verbs_finder.find_verb(full_sentence)
    if verb == "":
        return "", "", ""

    if verbs_finder.is_base_verb(verb):
        return "do not " + verb, index, words

    if verbs_finder.is_past_simple_verb(verb):
        return "did not " + verbs_finder.get_base_verb_by_past_simple(verb), index, words

    if verbs_finder.is_pres_simple_verb(verb):
        return "does not " + verbs_finder.get_base_verb_by_pres_simple(verb), index, words
    return "", "", ""


def construct_negative_sentence(index, words, negative_form):
    result = ""
    for i in range(0, index):
        result += (words[i] + " ")
    result += (negative_form + " ")
    if len(words) == 2:
        return result[0:len(result) - 1]
    for i in range(index + 1, len(words) - 1):
        result += (words[i] + " ")
    result += words[len(words) - 1]
    return result


def get_negative_sentence(sentence, verbs_finder):
    if " not " in sentence:
        negative = sentence.replace("not ", "")
        return negative

    # check all tenses apart from past and present simple :
    verb, index, words = find_tense_verb(sentence)
    if verb != "":
        return construct_negative_sentence(index, words, words[index] + " not")

    # check past simple and present simple :
    negative_verb, index, words = get_negative_verb(sentence, verbs_finder)
    if negative_verb != "":
        return construct_negative_sentence(index, words, negative_verb)

    # any verb haven't been found :
    return ""
