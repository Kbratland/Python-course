from requests import *
# file downloader
urlToFile = "https://www.nasa.gov/wp-content/uploads/2023/11/nhq202306210039orig.jpg"
src = get(urlToFile)
try:
    src.raise_for_status()
except Exception as e:
    print(f"Fail is {e}")
    exit()
# open file to save to
imgFile = open("nasaImage.jpg","wb")
# loop through source by chunk
for chunk in src.iter_content(100000):
    imgFile.write(chunk)
# close save file
imgFile.close()