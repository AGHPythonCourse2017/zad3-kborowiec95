import urllib.request


class Verb:
    def __init__(self, base, past_form, s_es_from):
        self.base = base
        self.past_simple_form = past_form
        self.present_simple_form = s_es_from

    def base_form(self):
        return self.base

    def past_simple(self):
        return self.past_simple_form

    def present_simple(self):
        return self.present_simple_form

    def __str__(self):
        return str(self.base) + " , " + str(self.past_simple_form) + " , " + str(self.present_simple_form)


class VerbsFinder:
    def __init__(self):
        url = "http://www.worldclasslearning.com/english/five-verb-forms.html"
        self.html = urllib.request.urlopen(url).read().decode("utf-8")
        self.verbs = []
        self.parse_html()

    def parse_html(self):
        # append 1st verb :
        self.verbs.append(Verb("abate", "abated", "abates"))
        lines = self.html.split("><a>1</a></td>")[1].split(">zooming<")[0].split("\n")
        lines = lines[1:3263] + lines[3271:len(lines)]
        self.verbs.append(Verb("abash", "abashed", "abashes"))

        # append from 2nd to 1000th verb :
        for i in range(1, 1000):
            base = lines[8 * i].split(">")[1].split("</")[0]
            past = lines[8 * i + 1].split(">")[1].split("</")[0]
            pres = lines[8 * i + 3].split(">")[1].split("</")[0]
            self.verbs.append(Verb(base, past, pres))

    def get_negative_verb(self, sentence):
        words = sentence.split(" ")
        # TODO : verbs are sorted do use binary search
        for i in range(0, len(words)):
            for vrb in self.verbs:
                if words[i] == vrb.base_form():
                    return "do not " + vrb.base_form(), i, words
                elif words[i] == vrb.past_simple():
                    return "did not " + vrb.base_form(), i, words
                elif words[i] == vrb.present_simple():
                    return "does not " + vrb.base_form(), i, words
        return ""
