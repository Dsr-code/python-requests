import requests
from tqdm import tqdm



url = input("Enter the URL : ")
name = input("Enter the name of the file with entension : ")


with requests.get(url,stream=True) as r:
    r.raise_for_status()






    with open(name,"wb") as f:
        progress_bar =  tqdm(total=int(r.headers['Content-Length']))
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                f.write(chunk)
                progress_bar.update(512)
# progress_bar.close()

print("     File downloaded Successfully !!!        ")