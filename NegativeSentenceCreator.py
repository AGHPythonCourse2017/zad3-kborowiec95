import GoogleResultsGetter

tense_nouns = ["am", "are", "is",
               "was", "were",
               "has", "have", "had",
               "will", "would", "do", "did"]


def find_noun(sentence):
    words = sentence.split(" ")
    for i in range(0, len(words)):
        if words[i] in tense_nouns:
            return words[i], i, words
    return "", "", ""


def get_negative(sentence):
    noun, index, words = find_noun(sentence)
    if noun in tense_nouns:
        # creating sentence with 'not' :
        negative = ""
        for i in range(0, index):
            negative += (words[i] + " ")
        negative += (noun + " not ")
        for i in range(index + 1, len(words) - 1):
            negative += (words[i] + " ")
        negative += words[len(words) - 1]
        return negative
    gs = GoogleResultsGetter.google_searcher()
    present_simple_num = gs.number_of_google_searches("don't "+sentence)
    past_simple_num = gs.number_of_google_searches("didn't "+sentence)
    if present_simple_num > past_simple_num:
        return "don't "+sentence
    else:
        return "didn't "+sentence
