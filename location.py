import json
import requests
import datetime

#IPkey = "058cab81b4a3a19201f37df18dab106616b562a860566e0aed5e9e15"
#IPkey = "d1cada6db96691cdb7699f2dac3f7652"
baseURL = "https://api.db-ip.com/v2/free/"
#ip = '49.207.55.34'
ip = '49.207.54.80'
def data(ip):
    path= f"{baseURL}{ip}"
    print(path)
    
    data = requests.get(path)
    jsondata=json.loads(data.text)
    print(jsondata)
    return jsondata

data(ip)

print(datetime.datetime.now())
'''def location(cords):
    a=reverse_geocoder.search(cords)
    pprint.pprint(a)

cords = (12.971599,77.594566)
#location(cords)'''
    

    
