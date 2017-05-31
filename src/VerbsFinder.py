import urllib.request
from bisect import bisect_left

tense_verbs = ["am", "are", "is",
               "was", "were",
               "has", "have", "had",
               "will", "would", "do", "did"]


def find_tense_verb(sentence):
    words = sentence.split(" ")
    for i in range(0, len(words)):
        if words[i] in tense_verbs:
            return words[i], i, words
    return ""


class VerbsFinder:
    def __init__(self):
        url = "http://www.worldclasslearning.com/english/five-verb-forms.html"
        self.html = urllib.request.urlopen(url).read().decode("utf-8")
        self.verbs_list_base = []
        self.verbs_list_past_simple = []
        self.verbs_list_pres_simple = []
        self.parse_html()

    def parse_html(self):
        # append 1st verb :
        self.verbs_list_base.append("abate")
        self.verbs_list_past_simple.append("abated")
        self.verbs_list_pres_simple.append("abates")
        lines = self.html.split("><a>1</a></td>")[1].split(">zooming<")[0].split("\n")
        lines = lines[1:3263] + lines[3271:len(lines)]

        # append from 2nd to 1000th verb :
        for i in range(1, 1000):
            base = lines[8 * i].split(">")[1].split("</")[0]
            past = lines[8 * i + 1].split(">")[1].split("</")[0]
            pres = lines[8 * i + 3].split(">")[1].split("</")[0]
            self.verbs_list_base.append(base)
            self.verbs_list_past_simple.append(past)
            self.verbs_list_pres_simple.append(pres)

    @staticmethod
    def binary_search(lst, x, left=0, right=None):
        right = right if right is not None else len(lst)
        pos = bisect_left(lst, x, left, right)
        return pos if pos != right and lst[pos] == x else -1

    def is_base_verb(self, word):
        return self.binary_search(self.verbs_list_base, word) != -1

    def is_pres_simple_verb(self, word):
        return self.binary_search(self.verbs_list_past_simple, word) != -1

    def is_past_simple_verb(self, word):
        return self.binary_search(self.verbs_list_pres_simple, word) != -1

    def find_verb(self, sentence):
        tense = find_tense_verb(sentence)
        if tense != "":
            return tense[0], tense[1]
        words = sentence.split(" ")
        for i in range(0, len(words)):
            v = words[i]
            if self.is_base_verb(v) or self.is_pres_simple_verb(v) or self.is_past_simple_verb(v):
                return v, i
        return ""
