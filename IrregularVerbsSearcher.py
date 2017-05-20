from random import randint


class Verb:
    def __init__(self, line):
        line = line[0:len(line) - 1]  # remove \n from the end of the line
        words = line.split("-")
        self.first = words[0]
        self.second = words[1].split("/")
        self.third = words[2].split("/")

    def get_first(self):
        return self.first

    def get_second(self):
        return self.second

    def get_third(self):
        return self.third

    def __str__(self):
        return self.first + " , " + str(self.second) + " ," + str(self.third)


def get_verbs_list():
    result = []
    with open("ps_irregular_verbs", 'r') as vrbs:
        lines = vrbs.readlines()
    for line in lines:
        result.append(Verb(line))
    return result


def first_form_past_simple(verb):
    irregular_verbs = get_verbs_list()
    for irr_verb in irregular_verbs:
        for second_form in irr_verb.get_second():
            if verb.endswith(second_form):
                prefix = verb[0:len(second_form)-1]
                return prefix + irr_verb.get_first()
    if verb.endswith("ed"):
        delete_e = randint(0, 1)
        if delete_e:
            return verb[0:len(verb) - 2]
        else:
            return verb[0:len(verb) - 1]
    return ""


print(first_form_past_simple("come in"))
