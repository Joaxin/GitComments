import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

file=open('C:\\ifasta.txt','w')
url='https://www.ncbi.nlm.nih.gov/gene/?term=ketoacyl-CoA+synthase+Gossypium+hirsutum'
print(url)
geneurl='https://www.ncbi.nlm.nih.gov'
data=[]
html=urllib.request.urlopen(url)
soup=BeautifulSoup(html,"lxml")
geneurllist=[]
for i in soup.find('tbody').findAll('tr'):
    geneurllist.append(geneurl+i.find('a')['href'])

print(geneurllist)

fastaurl=[]
for i in geneurllist:
    html=urllib.request.urlopen(i)
    soup=BeautifulSoup(html,"lxml")
    # print(soup1.findAll('h1')[1].get_text().replace('[','').replace(']','').strip())
    temp=soup.findAll('a')
    for i in temp:
        if i.get_text()=='FASTA':
            if 'report' in i['href']:
                fastaurl.append(geneurl+i['href'].replace("fasta","fasta&log$=seqview&format=text"))
                break


print(fastaurl)
#
# fastaurl=['https://www.ncbi.nlm.nih.gov/nuccore/NC_000913.3?report=fasta&log$=seqview&format=text&from=1150670&to=1151404', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_004330.1?report=fasta&log$=seqview&format=text&from=936858&to=938335&strand=true', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_000963.1?report=fasta&log$=seqview&format=text&from=955097&to=955822', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_004129.6?report=fasta&log$=seqview&format=text&from=1998747&to=1999487', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_000964.3?report=fasta&log$=seqview&format=text&from=2018554&to=2019270&strand=true', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_004347.2?report=fasta&log$=seqview&format=text&from=2898179&to=2898925&strand=true', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_019362.1?report=fasta&log$=seqview&format=text&from=16865&to=17617', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_002516.2?report=fasta&log$=seqview&format=text&from=3325379&to=3326122&strand=true', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_004307.2?report=fasta&log$=seqview&format=text&from=1139109&to=1139849&strand=true', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_005027.1?report=fasta&log$=seqview&format=text&from=5149549&to=5150355&strand=true', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_005027.1?report=fasta&log$=seqview&format=text&from=158031&to=158789', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_004337.2?report=fasta&log$=seqview&format=text&from=1138387&to=1139121', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_011852.1?report=fasta&log$=seqview&format=text&from=853961&to=854686', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_021082.1?report=fasta&log$=seqview&format=text&from=348580&to=349308&strand=true', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_021082.1?report=fasta&log$=seqview&format=text&from=205987&to=206709', 'https://www.ncbi.nlm.nih.gov/nuccore/NZ_CP006694.1?report=fasta&log$=seqview&format=text&from=1811505&to=1812275&strand=true', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_021175.1?report=fasta&log$=seqview&format=text&from=1634806&to=1635504&strand=true', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_015558.1?report=fasta&log$=seqview&format=text&from=312048&to=312746', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_009785.1?report=fasta&log$=seqview&format=text&from=1523951&to=1524649&strand=true', 'https://www.ncbi.nlm.nih.gov/nuccore/NC_015435.1?report=fasta&log$=seqview&format=text&from=1145232&to=1145954']
fasta=[]
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:25.0) Gecko/20100101 Firefox/25.0 "
)
driver=webdriver.PhantomJS(executable_path='G:\\Python\\web\\tools\\phantomjs\\bin\\phantomjs.exe',desired_capabilities=dcap)
# cap_dict = driver.desired_capabilities
# for key in cap_dict:
#     print('%s: %s' % (key, cap_dict[key]))
# print(driver.current_url)
for url in fastaurl:
    print(url)
    driver.get(url)
    time.sleep(3)
    fasta.append(driver.find_element_by_id('viewercontent1').text)
    # try:
    #     element = WebDriverWait(driver, 25).until(
    #         EC.presence_of_element_located((By.ID, "viewercontent1"))
    #     )
    #     fasta.append(driver.find_element_by_id('viewercontent1').text)
    #     print(fasta)
    # finally:
    #     driver.close()
driver.close()

for i in fasta:
    file.write(i+"\n")
file.close()