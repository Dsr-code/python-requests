import requests
from PIL import Image
from io import BytesIO

r=  requests.get("url of the image")

i = Image.open(BytesIO(r.content))    # creating a object

fp = open("img.jpg","wb")             # creating a file pointer
i.save()                              # saving the image
fp.close()                            # closing the file pointer
