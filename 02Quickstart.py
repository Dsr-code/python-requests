import requests

url="https://www.codewithharry.com"
r = requests.get(url)

#We can print these methods to know :

r.status_code     # to print the status code of the web site
r.headers['content-type']     # to print the headers and the content type of the web site
r.encoding      # to print the type of encoding used in the web site
r.text     # to print the text of the web site
r.json     # to get the content in json format