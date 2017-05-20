import IrregularVerbsSearcher

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


def find_past_simple_verb(sentence):
    words = sentence.split(" ")
    for i in range(0, len(words)):
        first_form = IrregularVerbsSearcher.first_form_past_simple(words[i])
        if first_form != "":
            return first_form, i, words
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

    # check past simple :
    verb, index, words = find_past_simple_verb(sentence)
    if verb != "":
        # creating sensence with 'did not' and first form of verb
        return create_negative(index, words, "did not " + verb)

    return ""
    # try in present simple :


print(get_negative("I distroyed my car"))