import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

# https://www.ncbi.nlm.nih.gov/gene/?term=Gossypium++arboreum+3-ketoacyl-CoA+synthase
# https://www.ncbi.nlm.nih.gov/gene/?term=Gossypium+raimondii+3-ketoacyl-CoA+synthase
# https://www.ncbi.nlm.nih.gov/gene/?term=arabidopsis+thaliana+3-ketoacyl-CoA+synthase
file=open('C:\\ifasta.txt','w')
import requests
payload = {'EntrezSystem2.PEntrez.Gene.Gene_ResultsPanel.Gene_DisplayBar.PageSize': '100'}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}
url = requests.post("https://www.ncbi.nlm.nih.gov/gene/?term=ketoacyl-CoA+synthase+Gossypium+hirsutum", data=payload,headers = headers)
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
# fasta=[]
# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap["phantomjs.page.settings.userAgent"] = (
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
# )
# driver=webdriver.PhantomJS(executable_path='G:\\Python\\web\\tools\\phantomjs\\bin\\phantomjs.exe',desired_capabilities=dcap)
# for url in fastaurl:
#     print(url)
#     driver.get(url)
#     time.sleep(3)
#     fasta.append(driver.find_element_by_id('viewercontent1').text)
# driver.close()
#
# for i in fasta:
#     file.write(i+"\n")
# file.close()