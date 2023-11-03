from webbrowser import *
from requests import *
from bs4 import *

result = get("https://riverdaleschool.com/")
try:
    result.raise_for_status()
except Exception as e:
    print(f"Error retrieving webpage: {e}")
    exit()
    
newSoup = BeautifulSoup(result.text,'html.parser')
newsElement = newSoup.select('.home-news .fsTitle')
linkElement = newSoup.select('.home-news .fsTitle a')
#Get titles
for headline in newsElement:
    print(headline.getText().strip() + " - opening!")
for link in linkElement:
    open(link.attrs["href"])
#Get links and addresses to open tabs with each