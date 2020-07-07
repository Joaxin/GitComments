#! python3
# downloadXkcd.py - Downloads every single XKCD comic.

import requests, os, bs4,re

url = 'https://xkcd.com' # starting url
schema = 'https:'

os.makedirs('xkcd', exist_ok=True) # store comics in ./xkcd

## https://xkcd.com/# 表示没有漫画了哦，循环结束
while not url.endswith('#'):
    ## 要下载的漫画的网址
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,'lxml')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    ## 有一些 XKCD 页面有特殊的内容，不是一个简单的图像文件，可以跳过
    if comicElem == []:
        print(' Could not find comic image from %s.'%(url))
    else:
        comicUrl = comicElem[0].get('src')
        # Download the image.
        print('Downloading image %s...' % (schema + comicUrl))
        res = requests.get(schema + comicUrl)
        res.raise_for_status()
        ## 保存图片到 ./xkcd
        ## 比如//imgs.xkcd.com/comics/dynamic_entropy.png
        ## 保存为dynamic_entropy.png
        imageFile = open(os.path.join('xkcd', re.sub("\D", "", url) + '_' + os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'https://xkcd.com' + prevLink.get('href')

print('Done.')
