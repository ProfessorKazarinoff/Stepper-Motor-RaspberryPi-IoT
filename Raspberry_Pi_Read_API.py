import requests
from API_key import API_KEY
# API_KEY withheld for serurity reasons
# function will read thingspeak and will be able to be called into another file

def read_api():
    base_url = 'https://api.thingspeak.com/channels/'
    channel_number = '710933'
    mid_url = '/fields/'
    field_number = '1'
    json_url = '.json?api_key='
    key = API_KEY
    end_url = '&results='
    results = '1'

    url = base_url+channel_number+mid_url+field_number+json_url+API_KEY+end_url+results

    r = requests.get(url)
    json_data = r.json()
    # Data will fetch the data from thingspeak, returning either a 1 or a 0
    Data = json_data['feeds'][0]['field1']

    return(data)
