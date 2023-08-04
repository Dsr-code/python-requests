import requests

url="https://www.codewithharry.com"
r= requests.get(url)
# print(r.text)

with open("index.html", "w") as f:
    f.write(r.text)
