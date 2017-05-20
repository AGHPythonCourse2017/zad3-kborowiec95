import urllib.request
import urllib.error


class GoogleResultsGetter:
    def __init__(self, google_api_user_key, custom_search_id):
        self.key = google_api_user_key
        self.custom_search_id = custom_search_id

    def get_from_api(self, request):
        google_request = request.replace(" ", "+")
        url = "https://www.googleapis.com/customsearch/v1?key=" + self.key + \
              "&cx=" + self.custom_search_id + \
              "&q=" + google_request
        return urllib.request.urlopen(url).read().decode("utf-8")

    def number_of_google_searches(self, sentence):
        for json_line in self.get_from_api(sentence).split("\n"):
            if "totalResults" in json_line:
                return int(json_line.split("\"")[3])
        raise ValueError("Wrong json format")


def google_searcher():
    return GoogleResultsGetter("AIzaSyCZ9HvClGcCYqVxT9SruazjoHb9xNewuOM", "008201436329454125027:r1b12zwr7ko")
