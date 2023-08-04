import requests

url = "url to the exe"

r = requests.get(url)
fp=open("fileName.exe", "wb")
fp.write(r.content)
fp.close()
