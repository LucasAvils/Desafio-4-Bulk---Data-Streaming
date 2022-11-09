import json
import xmltodict
import requests
import time

from os import path, sep
import os

file ='tempo1.xml'
location = 'D:\Projetos\Desafio 4 Bulk - Data Streaming'
path = os.path.join(location, file)
i=0
count = 24
url = 'https://w1.weather.gov/xml/current_obs/PADQ.xml'

while i < count:
    r = requests.get(url,allow_redirects=True)
    o = open('tempo1.xml','wb').write(r.content)
    with open('tempo1.xml') as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        json_data = json.dumps(data_dict)
        with open("data.json","a") as json_file:
            json_file.write(json_data + '\n')
    os.remove(file)
    i+=1
    time.sleep(3600)
    
    