import requests

url = "url to the mp3"

r = requests.get(url)

fp = open("music.mp3", "wb")
fp.write(r.content)
fp.close()