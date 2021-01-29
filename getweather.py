from bs4 import BeautifulSoup
import re
import requests

def getData(cityname):
    # cityname = '13001BOKARO'
    # cityname = '13003GIRIDIH'
    # sitedata = requests.post('https://city.imd.gov.in/citywx/city_weather.php', data={'id':'13001BOKARO'})
    sitedata = requests.post('https://city.imd.gov.in/citywx/city_weather.php', data={'id' : cityname})
    print(sitedata.status_code)
    bsitedata = BeautifulSoup(sitedata.text, features= 'html.parser')

    data = { 'today': {}, 'next7days' : {} }

    textdata = bsitedata.text.strip()
    textdata_list = re.sub(r'\s\s+','\n',textdata).split('\n')
    for i in range(4,26,2):
        data['today'][textdata_list[i]] = textdata_list[i+1]
        print(textdata_list[i]+':',textdata_list[i+1])

    print()

    day = 0
    for i in range(31,59,4):
        data['next7days'][f'day{day}'] = textdata_list[i:i+4]
        print(textdata_list[i],textdata_list[i+1],textdata_list[i+2],':',textdata_list[i+3])
        day+=1

    return data


