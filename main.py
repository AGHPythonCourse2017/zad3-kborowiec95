from GoogleResultsGetter import *

gs = google_searcher()

try:
    true_score = gs.number_of_google_searches("Cracow is in Poland")
    false_score = gs.number_of_google_searches("Cracow is not in Poland")
    print("This message is true for : " + str(true_score) + " vs " + str(false_score) + " true vs false")
except urllib.error.URLError:
    print("Connection problems")
except ValueError:
    print("Wrong result")
