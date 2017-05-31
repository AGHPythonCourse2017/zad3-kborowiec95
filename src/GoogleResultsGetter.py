import urllib.request
import urllib.error


class GoogleResultsGetter:
    def __init__(self, google_api_user_key, custom_search_id):
        self.key = google_api_user_key
        self.custom_search_id = custom_search_id

    @staticmethod
    def create_google_request(request):
        return request.replace(" ", "+")

    def create_url(self, google_request):
        return "https://www.googleapis.com/customsearch/v1?key=" + self.key + \
               "&cx=" + self.custom_search_id + \
               "&q=" + google_request

    def get_from_api(self, request):
        google_request = self.create_google_request(request)
        url = self.create_url(google_request)
        return urllib.request.urlopen(url).read().decode("utf-8")

    def number_of_google_searches(self, sentence):
        for json_line in self.get_from_api(sentence).split("\n"):
            if "totalResults" in json_line:
                return int(json_line.split("\"")[3])
        raise ValueError("Wrong json format")
