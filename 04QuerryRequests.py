import requests

url="https://httpbin.org/post"
r = requests.post(url, data={'key':'value'})

# NOTE -  this is same as :
# https://httpbin.org/post?key1=key&key2=value 

# print(r.text)

# we san also use the auth parameter to give the authentication for user and password
