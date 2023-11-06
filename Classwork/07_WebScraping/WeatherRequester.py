from requests import *
from bs4 import *
from pyperclip import *

result = get("https://www.wunderground.com/weather/us/or/portland/KORPORTL605")

try:
    result.raise_for_status()
except Exception as e:
    print(f"Error retrieving webpage: {e}")
    exit()

newSoup = BeautifulSoup(result.text, 'html.parser')
highFind = newSoup.select(".hi-lo .hi")
lowFind = newSoup.select(".hi-lo .lo")
currentFind = newSoup.select(".current-temp")
feelsFind = newSoup.select(".feels-like")
weathFind = newSoup.select(".weather-quickie")
weath2Find = newSoup.select(".wx-value")
print("The high for today is " + highFind[0].getText())
print("The low for today is " + lowFind[0].getText())
print("The current temperature is " + currentFind[0].getText())
print("Feels" + feelsFind[0].getText())
print(weathFind[0].getText())
print("The weather today is " + weath2Find[1].getText())
