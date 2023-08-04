import requests

url = "https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-623.exe"

r = requests.get(url,stream=True)
totalExpectedBytes = int(r.headers['content-Length'])
# print(totalExpectedBytes)

bytesRecieved = 0

with open("winnrar.exe", "wb") as f:
    for chunk in r.iter_content(chunk_size=128):
        print(f"{bytesRecieved} out of {totalExpectedBytes}")
        f.write(chunk)
        bytesRecieved += 128
