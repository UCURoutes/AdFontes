import urllib.request
import urllib.parse
import json
import URL
YOUR_API_KEY = "AIzaSyD_N4NN2k3G1lM9SAhV5WNA07Mvu27747g "
class ExceptionOfType(Exception):
    pass

def get_type():
    key = input("Enter your type[bar,museum,night_club,doctor ]: ")
    if type(key) == str and key in ["book_store","bar","airport","museum","night_club","doctor"]:
        return key
    else:
        return get_type()
        #raise ExceptionOfType("Your type must be in list of types, or you have write it in incorect way  !!!")

def get_data_from_URL(base_url):
    '''
    It gets data from API Google Places 
    '''
    request_url = base_url
    request = urllib.request.Request(request_url)
    with urllib.request.urlopen(request_url) as response:
        data = response.read()
        data = data.decode("utf-8")
        json.loads(data)
    return data

def loading_data_from_jason(begin):
    url = URL.URLclass(location=str(begin[0]) + "," + str(begin[1]), type=get_type(), rad=5000,
                       Yure_key=YOUR_API_KEY,
                       BASE_URL="https://maps.googleapis.com/maps/api/place/radarsearch/json?")
    BASE_URL = url.get_url_with_lat_and_lng_by_hend()
    data = json.loads(get_data_from_URL(BASE_URL))
    return data