#import requests

#url = "https://community-open-weather-map.p.rapidapi.com/weather"

#querystring = {"q":"London,uk","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"\"metric\" or \"imperial\"","mode":"xml, html"}

#headers = {
#    'x-rapidapi-key': "2203c826a3msh6e036bab1ff9affp1515f5jsnc92b0dd749ab",
#    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
#    }

#response = requests.request("GET", url, headers=headers, params=querystring)
response_test = 'test({"coord":{"lon":-0.1257,"lat":51.5085},"weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],"base":"stations","main":{"temp":274.59,"feels_like":270.15,"temp_min":273.71,"temp_max":275.37,"pressure":994,"humidity":93},"visibility":10000,"wind":{"speed":3.6,"deg":250},"clouds":{"all":90},"dt":1611504890,"sys":{"type":1,"id":1414,"country":"GB","sunrise":1611474590,"sunset":1611506106},"timezone":0,"id":2643743,"name":"London","cod":200})'


def getValueFromString(word, word2, str):
    word_index = str.find(word)
    str = str[word_index:]
    word_index = str.find(word2)
    str = str[word_index + len(word2):]
    str = str[str.find('"')+1:]
    str = str[str.find('"')+1:]
    return str[:str.find('"')]



print(getValueFromString("weather", "main", response_test))
print(getValueFromString("visibility", "wind", response_test))
print(getValueFromString("weather", "id", response_test))





#print(response.text)
print(response_test)
