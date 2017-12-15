import urllib.request
import urllib.parse
import json
import Loading
YOUR_API_KEY = "AIzaSyD_N4NN2k3G1lM9SAhV5WNA07Mvu27747g "
#####################
#####################
##################### "https://maps.googleapis.com/maps/api/place/details/json?"
class URLclassInfo:
    def __init__(self,placeid,Yure_key,BASE_URL="https://maps.googleapis.com/maps/api/place/details/json?"):
        self.BASE_URL = BASE_URL
        self.Yure_key =Yure_key
        self.placeid=placeid
    def request_url(self):
        return self.BASE_URL+"placeid="+self.placeid+"&key="+self.Yure_key



def get_data_from_URL(placeid):
    '''
    It gets data from API Google Places 
    '''

    request_url = URLclassInfo(placeid,YOUR_API_KEY).request_url()
    request = urllib.request.Request(request_url)
    with urllib.request.urlopen(request_url) as response:
        data = response.read()
        data = data.decode("utf-8")
        json.loads(data)
    return data
def get_json(placeid):
    return json.loads(get_data_from_URL(placeid))
