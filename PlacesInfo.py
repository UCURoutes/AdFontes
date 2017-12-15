import Loading
import URL
import URLpacesInfo

def data_corector(data):
    dct = {}
    for i in data:
        dct[(i['geometry']['location']['lat'], i['geometry']['location']["lng"])] = i['place_id']
    return dct

##############################
##############################
##############################
def dct_of_rait_and_location(data_dct):
    dct = {}
    for i in data_dct:
        try:
            dct[i] = URLpacesInfo.get_json(data_dct[i])['result']['rating']
        except KeyError:
            dct[i] = None
    return dct

def get_data_from_URL(begin):
    data = Loading.loading_data_from_jason(begin)
    data = data['results']
    data_dct = data_corector(data)
    dct = dct_of_rait_and_location(data_dct)
    return dct
