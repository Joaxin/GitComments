import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

file=open('C:/Users/Lyole/Desktop/ncbi.txt','w')
import requests
payload = {'EntrezSystem2.PEntrez.Gene.Gene_ResultsPanel.Gene_DisplayBar.PageSize': '100'}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
url = requests.post("http://www.xiami.com/genre/songs/sid/225?spm=a1z1s.3057857.0.0.0pCi9a", data=payload,headers = headers)
geneurl='https://www.ncbi.nlm.nih.gov'
data=[]
soup=BeautifulSoup(url.text,"lxml")
geneurllist=[]
for i in soup.find('tbody').findAll('tr'):
    geneurllist.append(geneurl+i.find('a')['href'])

print(geneurllist)

fastaurl=[]
for i in geneurllist:
    html=urllib.request.urlopen(i)
    soup=BeautifulSoup(html,"lxml")
    temp=soup.findAll('a')
    for i in temp:
        if i.get_text()=='FASTA':
            if 'report=fasta' in i['href']:
                fastaurl.append(geneurl+i['href'].replace("fasta","fasta&log$=seqview&format=text"))
                print(fastaurl)
                break
