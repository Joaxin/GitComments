
# coding: utf-8

# In[ ]:


# Xiami Jazz - Hiphop Artists python Spider

import json
import requests
import re
import time
import csv

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'www.xiami.com',
    'Cookie': 'gid=149362618428663; _unsign_token=1adc7389ae8c232e7e54662f85556612; cna=WEhZEclvUUACAXPEmO9Y2uTU; __utma=251084815.2116239786.1493626546.1493626546.1493626546.1; bdshare_firstime=1495602348897; l=AvPzpV4ym6gxy8lGs7rmZxELA/wc/ofq; _xiamitoken=a011f1a247a74d6b4fd2eff8de3a2ef9; login_method=emaillogin; XMPLAYER_url=/song/playlist/id/1/type/9; XMPLAYER_addSongsToggler=0; XMPLAYER_volumeValue=0.18; user_from=1; t_sign_auth=4; join_from=1ziRHIke6zg; member_auth=0z2bHYkd6j8x0ffASoo0JiZLtbLWE2CHkoxVirF5tgUkLYZdN4D8lquQQAtN0CWRrWHJlxZIV62biVyKvGI; user=12058525%22%E6%B3%9B%E4%BA%A6%E5%A6%82%E7%A7%8B%22images%2Favatar_new%2F241%2F56ac6f7ea0bab_12058525_1454141310_1.png%220%224116%22%3Ca+href%3D%27http%3A%2F%2Fwww.xiami.com%2Fwebsitehelp%23help9_3%27+%3ELv6%3C%2Fa%3E%2210%221%224307%223def422098%221520839375; XMPLAYER_isOpen=1; __guestplay=MTc3MDE3MzQ5NywzOzE3NzE5Njc5NDAsMTsxNzcxMzYyOTIxLDI7MTc2OTg1NTQ5NiwyOzE3NjkxOTY2NjksMjsyMDgyNjcxLDI7MTc5NTU1MTIxNiwyOzE4MDEzNjE1MDEsMjsxMDYyMjQzLDI7MTc2OTE4MjcxMiwyOzE3NzA5ODUzNTEsMjsxNzczODQzMzIzLDI7MzY1NzA1MSwyOzE3Njk5Nzc0NjEsMjsxNzczMzUxMjQ0LDI7MzYzMzM5MSwyOzE3NzQwMjA1MTcsMjsxNzcyNjA1MTg1LDI7MTc3MjU2MzIwNCwyOzExMzczNCwyOzE3NzI1NTk2NzYsMg%3D%3D; isg=BEJCOa-wrLsDHLA7VAV0p_zgk0hku90pgD7CoYxbbrVg3-JZdKOWPcgdi9ujlL7F',
    'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 YaBrowser/18.2.0.284Yowser/2.5 Safari/537.36'
}

redirectHeaders = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'i.xiami.com',
    'Cookie': 'gid=149362618428663; _unsign_token=1adc7389ae8c232e7e54662f85556612; cna=WEhZEclvUUACAXPEmO9Y2uTU; __utma=251084815.2116239786.1493626546.1493626546.1493626546.1; bdshare_firstime=1495602348897; l=AvPzpV4ym6gxy8lGs7rmZxELA/wc/ofq; _xiamitoken=a011f1a247a74d6b4fd2eff8de3a2ef9; login_method=emaillogin; XMPLAYER_url=/song/playlist/id/1/type/9; XMPLAYER_addSongsToggler=0; XMPLAYER_volumeValue=0.18; user_from=1; t_sign_auth=4; join_from=1ziRHIke6zg; member_auth=0z2bHYkd6j8x0ffASoo0JiZLtbLWE2CHkoxVirF5tgUkLYZdN4D8lquQQAtN0CWRrWHJlxZIV62biVyKvGI; user=12058525%22%E6%B3%9B%E4%BA%A6%E5%A6%82%E7%A7%8B%22images%2Favatar_new%2F241%2F56ac6f7ea0bab_12058525_1454141310_1.png%220%224116%22%3Ca+href%3D%27http%3A%2F%2Fwww.xiami.com%2Fwebsitehelp%23help9_3%27+%3ELv6%3C%2Fa%3E%2210%221%224307%223def422098%221520839375; XMPLAYER_isOpen=1; __guestplay=MTc3MDE3MzQ5NywzOzE3NzE5Njc5NDAsMTsxNzcxMzYyOTIxLDI7MTc2OTg1NTQ5NiwyOzE3NjkxOTY2NjksMjsyMDgyNjcxLDI7MTc5NTU1MTIxNiwyOzE4MDEzNjE1MDEsMjsxMDYyMjQzLDI7MTc2OTE4MjcxMiwyOzE3NzA5ODUzNTEsMjsxNzczODQzMzIzLDI7MzY1NzA1MSwyOzE3Njk5Nzc0NjEsMjsxNzczMzUxMjQ0LDI7MzYzMzM5MSwyOzE3NzQwMjA1MTcsMjsxNzcyNjA1MTg1LDI7MTc3MjU2MzIwNCwyOzExMzczNCwyOzE3NzI1NTk2NzYsMg%3D%3D; isg=BEJCOa-wrLsDHLA7VAV0p_zgk0hku90pgD7CoYxbbrVg3-JZdKOWPcgdi9ujlL7F',
    'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 YaBrowser/18.2.0.284Yowser/2.5 Safari/537.36'
}


def Xiami(url):
    s = requests.Session()
    try:
        r = s.get(url, headers=headers, allow_redirects=True)
        if r.status_code == 200:
            return r.content.decode("utf8", "ignore")
        else:
            if response.history:
                #                 for his in r.history:
                #                     print (his.status_code, his.url)
                print("Request was redirected to ", r.url)
                try:
                    rr = s.get(r.url, headers=redirectHeaders)
                    rr.encoding = 'utf-8'
                    if rr.status_code == 200:
                        return rr.content.decode("utf8", "ignore")
                    return(rr.status_code)
                except RequestException:
                    return "Redirected, But Some Still thing Wrong!!!"
    except RequestException:
        return "ERROR!!!"

# TEST
# shrimp = Xiami('http://www.xiami.com/artist/bn8fcff15')
# print(shrimp)


def Xiami_parse(text):
    pat1 = re.compile(
        '<div.*?artist.*?image.*?src="(.*?)".*?info.*?href="(.*?)".*?>(.*?)</a>.*?</div>', re.S)
    pat2 = 'artist_info.*?top.*?top.*?>(.*?)</td>'
    items = re.findall(pat1, text)
    for i in range(len(items)):  # for artists  country
        items[i] = list(items[i])
        items[i][1] = 'http://www.xiami.com' + items[i][1]
        artist = Xiami(items[i][1])
        if len(str(artist)) <= 10:  # if ERROR Artist Page
            print("------------WRONG-----------", "\n", items[i][1])
            print(artist)
            items[i].append("")
            continue
        country = re.findall(pat2, artist, re.S)
        items[i].append(country[0])
        # print(items[i])
        time.sleep(1)
    return(items)


def main():
    for i in range(49):
        url = "http://www.xiami.com/genre/artists/sid/225/page/" + str(i + 1)
        Artists = Xiami_parse(Xiami(url))
        f = csv.writer(open('Art.csv', 'a', newline=""))
        print("Page ", i + 1)
        print(Artists)
        for artist in Artists:
            image = artist[0]
            url = artist[1]
            singer = artist[2]
            country = artist[3]
            f.writerow([image, url, singer.encode('gbk', 'ignore').decode('gbk'), country.encode('gbk', 'ignore').decode('gbk')])
        time.sleep(5)


if __name__ == '__main__':
    main()


# encoding test
# Artists = [['Under The Hood', 'http://www.xiami.com/artist/GQ37f56d', 'Think Twice', 'Canada 加拿大'], ['莲花', 'http://www.xiami.com/artist/IjN92555', '白天不亮', 'China 中国大陆'], ['Hypnotize Am7 Remix', 'http://www.xiami.com/artist/ccfz22af7', 'Am7', 'Japan 日本'], ['Passion Flower', 'http://www.xiami.com/artist/JnO679be', 'Prisma', 'Japan 日本'], ['Santana', 'http://www.xiami.com/artist/3YG770c4', 'Justice System', '欧美'], ['Children Of The Earth - Piano Mix', 'http://www.xiami.com/artist/b6N1e9342', 'Ayur', 'Japan 日本'], ['梦回还', 'http://www.xiami.com/artist/kdAEqg499a8', 'Kyle Xian', 'China 中国大陆'], ['你嫌命太长', 'http://www.xiami.com/artist/KsX738a3', 'Mr.Trouble', 'China 中国大陆'], ['Happy Home', 'http://www.xiami.com/artist/bn8B8T6de17', 'FrostyC', 'United States of America 美国'], ['Take It Easy', 'http://www.xiami.com/artist/nmSxZy673ef', '饺子', 'China 中国大陆'], ['删除',             'htp://www.xiami.com/artist/mNlyRp52fbc', 'BIHA', 'China 中国大陆'], ['在海边feat.德宏老爹', 'http://www.xiami.com/artist/eEhz51070', '卡姆路', 'China 中国大陆'], ['没有你（Without Ü）', 'http://www.xiami.com/artist/yhDuGcc0b56', 'gcolt', 'China 中国大陆'], ['与你 (With you)', 'http://www.xiami.com/artist/naVESS4ef35', 'Yee', 'China 中国大陆'], ['tik tok', 'http://www.xiami.com/artist/bpa42V860ac', '牛牛', 'China 中国大陆'], ['我想重复播放一首歌（42 feat.YoungJack）', 'http://www.xiami.com/artist/bVT9V557fd8', '满舒克', 'China 中国大陆'], ['兄弟情义', 'http://www.xiami.com/artist/mhJHOH79282', '正皇旗组合', 'China 中国大陆'], ['The Light', 'http://www.xiami.com/artist/buXA1c58b', 'Common', 'United States of America 美国'], ['Luv(sic)pt2 - Acoustica -', 'http://www.xiami.com/artist/ZJLb0dd9', 'Haruka Nakamura', 'Japan 日本'], ['Lamp Reason~yellow Contemporary Remix', 'http://www.xiami.com/artist/b5mNf5b10', 'WOODBLUE ', 'Japan 日本']]

# f = csv.writer(open('artists.csv', 'a', newline=""))  # # , encoding='utf-8'
# for artist in Artists:
#     opus = artist[0]
#     url = artist[1]
#     singer = artist[2]
#     country = artist[3]
# f.writerow([opus.encode('gbk', 'ignore').decode('gbk'), url,
# singer.encode('gbk', 'ignore').decode('gbk'), country.encode('gbk',
# 'ignore').decode('gbk')]
