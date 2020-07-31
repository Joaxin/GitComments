import requests
from requests.exceptions import RequestException
import os
import time
import json

header = {
		"cookie": "_ga=GA1.2.190494774.1538881112; PORTAL_VERSION=v4; qiniu_seo_refer=https://www.google.com.hk/; _gid=GA1.2.1655720767.1541766819; SSID=WjdCNElSQUU2UFZUTVNEQkJNRzExNEU0U1JCOE1aWUZIUDNZVSwxNTQxNzY2ODI0OTEzNjk5MjUyLDliMDg4NjAzNTYzOTI0YTk2MzNmYWVkMTZlODExMTY2MTE4NzY0MDFkZWQ0NzQ1MWM0NDU1NGRjNGJhZGJlYmNlODI0NzNiZDhlYTY4Yzg5MmE3MTk3MjFiNzgwZjk5MGQ1NjNmNmYzNThmZWFiNTQyY2JiYTIwNDIxOGZlYTg0; PORTAL_UID=1381281658;PORTAL_SESSION=T1lXSVEzMUNFTVFFWkQ4TUVNOVoyUks4TzRMRzE0VFgsMTU0MTc2NjgzMDkwMzY5NjUzNSxlNjMwOTVkYTM5MTZiZjZlMDEzYzBiOGMwOGZmZjc5MGI2ZWQxZTI3; gr_user_id=e95803a7-dab6-4f3c-8b2d-f03e374eb5c2; LXB_REFER=link.zhihu.com; Hm_lvt_204fcf6777f8efa834fe7c45a2336bf1=1541766819,1541768460,1541771097; Hm_lpvt_204fcf6777f8efa834fe7c45a2336bf1=1541771524",
        "User - Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "authority": "portal.qiniu.com",
        "Accept - Encoding": "gzip, deflate, br",
        "scheme" : "https",
    }
urls = "https://portal.qiniu.com/api/kodo/bucket/files?bucket=lofter&delimiter=&limit=50&marker="
    
def request_qiniu(url,header):
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            return response
        return None
    except RequestException:
        return None

marker = "&"
try:
    os.mkdir("lofter")
except OSError:
    pass
os.chdir("lofter")
sum = 0

while str(marker).strip()!= '':

    url = urls + marker
    res = request_qiniu(url, header)
    jsondata = json.loads(res.text)
    marker = jsondata['data']['marker']

    for i in range(0,len(jsondata['data']['entries'])):
        fileurl = jsondata['data']['entries'][i]['dl_url']
        print(str(i) + ": " + fileurl)
        filename = jsondata['data']['entries'][i]['key']
        print(filename)
        with open(filename, 'wb') as f:
            img = requests.get(fileurl).content
            f.write(img)
            time.sleep(0.1) 
            sum += 1
            print("写入数据，第"+str(sum)+"条：" + filename)