import urllib.request
from bisect import bisect_left


def binary_search(a, x, lo=0, hi=None):
    hi = hi if hi is not None else len(a)
    pos = bisect_left(a, x, lo, hi)
    return pos if pos != hi and a[pos] == x else -1


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
        for i in range(0, len(words)):
            index = binary_search(self.v_base, words[i])
            if index != -1:
                return "do not " + words[i], i, words

            index = binary_search(self.v_past_simple, words[i])
            if index != -1:
                return "did not " + words[i], i, words

            index = binary_search(self.v_pres_simple, words[i])
            if index != -1:
                return "does not " + words[i], i, words
        return ""
