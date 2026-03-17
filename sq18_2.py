import time,threading,multiprocessing
from concurrent.futures import ThreadPoolExecutor
import requests

def download(url,file):
    r=requests.get(url)
    with open(file,'wb') as f:
        f.write(r.content)



#  normal
url_list = ['https://www.python.org/static/community_logos/python-logo-master-v3-TM.png'] * 50

start=time.time()
for url,idx in enumerate(url_list):
    download(url,f'python_{idx}.png')

end=time.time()

#  multithreading
with ThreadPoolExecutor() as e:
    start1=time.time()
    list(e.map(download, url_list, [f'python_{idx}.png' for idx in range(len(url_list))]))
    end1=time.time()

#async await
async def download_async(url,file):
    r=requests.get(url)
    with open(file,'wb') as f:
        f.write(r.content)
    
print(f"Time taken for normal execution: {end - start} seconds")
print(f"Time taken for multithreading execution: {end1 - start1} seconds")


