import urllib.request
import urllib.error

api_key = "AIzaSyCZ9HvClGcCYqVxT9SruazjoHb9xNewuOM"
file_name = "sample_result"


def get_from_api(key, request):
    google_request = request.replace(" ", "+")
    url = "https://www.googleapis.com/customsearch/v1?key=" + key \
          + "&cx=008201436329454125027:r1b12zwr7ko&q=" + google_request
    return urllib.request.urlopen(url).read().decode("utf-8")
    #return url

def lines(json_text):
    return json_text.split("\n")


def get_from_file(name):
    with open(name, 'r') as json_text:
        res = json_text.read()
    return res


def get_number_of_google_searches(word):
    for line in lines(get_from_api(api_key, word)):
        if "totalResults" in line:
            return line.split("\"")[3]
    raise ValueError("Wrong json format")

try:
    true = int(get_number_of_google_searches("Pope is dead"))
    false = int(get_number_of_google_searches("Pope is not dead"))
    true_coefficient = true / (true + false) * 100
    print("This message is true for : " + str(true) + " vs " + str(false) + " true vs false")
except urllib.error.URLError:
    print("Connection problems")
except ValueError:
    print("Wrong result")
