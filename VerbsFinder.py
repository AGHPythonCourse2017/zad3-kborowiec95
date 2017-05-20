import urllib.request
from bisect import bisect_left


def binary_search(a, x, lo=0, hi=None):  # can't use a to specify default for hi
    hi = hi if hi is not None else len(a)  # hi defaults to len(a)
    pos = bisect_left(a, x, lo, hi)  # find insertion position
    return pos if pos != hi and a[pos] == x else -1 # don't walk off the end


class VerbsFinder:
    def __init__(self):
        url = "http://www.worldclasslearning.com/english/five-verb-forms.html"
        self.html = urllib.request.urlopen(url).read().decode("utf-8")
        self.v_base = []
        self.v_past_simple = []
        self.v_pres_simple = []
        self.parse_html()

    def parse_html(self):
        # append 1st verb :
        self.v_base.append("abate")
        self.v_past_simple.append("abated")
        self.v_pres_simple.append("abates")
        lines = self.html.split("><a>1</a></td>")[1].split(">zooming<")[0].split("\n")
        lines = lines[1:3263] + lines[3271:len(lines)]

        # append from 2nd to 1000th verb :
        for i in range(1, 1000):
            base = lines[8 * i].split(">")[1].split("</")[0]
            past = lines[8 * i + 1].split(">")[1].split("</")[0]
            pres = lines[8 * i + 3].split(">")[1].split("</")[0]
            self.v_base.append(base)
            self.v_past_simple.append(past)
            self.v_pres_simple.append(pres)

    def get_negative_verb(self, sentence):
        words = sentence.split(" ")
        # TODO : verbs are sorted do use binary search
        for i in range(0, len(words)):
            for vrb in self.v_base:
                if words[i] == vrb:
                    return "do not " + vrb, i, words
            for vrb in self.v_past_simple:
                if words[i] == vrb:
                    return "did not " + vrb, i, words
            for vrb in self.v_pres_simple:
                if words[i] == vrb:
                    return "does not " + vrb, i, words
        return ""
