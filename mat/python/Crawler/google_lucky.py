#! python3
# lucky.py - Opens several Google search results.

import requests, sys, webbrowser
from bs4 import BeautifulSoup

keywords = ' '.join(sys.argv[1:])
# for better search results
query = keywords.replace(' ', '+')
# display text while downloading the Google page
print('Googling...' + query) 

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
}

res = requests.get('https://google.com/search?q=' + query, headers = headers)
try:
    res.raise_for_status() ## 如果出错，将抛出异常
except Exception as exc: 
    print('There was a problem: %s' % (exc)) 
# Retrieve top search result links.
soup = BeautifulSoup(res.text,'lxml')
# Open a browser tab for each result.
linkElems = soup.select('div.rc>.r')
numOpen = min(10, len(linkElems))
results = []
for i in range(numOpen):
    link  = linkElems[i].select('a')[0].get('href')
    title  = linkElems[i].select('h3')[0].text
    item = {
            "title": title,
            "link": link
        }
    results.append(item)
    webbrowser.open(link)

print(results)