from urllib.request import urlopen
from bs4 import BeautifulSoup
import re


class Translator(object):
    markList = {"h1", "h2", "h3", "p"}

    def find_we_need(self, url):
        sourcePage = urlopen(url)
        bsObj = BeautifulSoup(sourcePage, "html.parser")
        #这个mw-navigation是萌娘百科的导航块，这么写就只能适用于萌娘百科了，很不爽，
        #以后用在其他网站的时候再想怎么兼容好了。
        bsObj.find('div', id = 'mw-navigation').decompose()
        contents = bsObj.findAll(self.markList)
        return contents

    def translate(self, sources):
        md_file = open("markdown.md", "w")
        for content in sources:
            # 直接取消html的换行符，自己加
            if re.search('</?br ?/?>', str(content)):
                continue

            # 萌娘百科吐槽特色用的删除线，其他网站应该有类似的
            elif re.search('<del>.*?</del>', str(content)):
                p = re.compile(r'</?del>')
                for a in p.split(str(content)):
                    if re.search(r'<.*?>', a) == None:
                        md_file.write('<del>' + a + '</del>')
                    else:
                        tbs = BeautifulSoup(a, "html.parser")
                        #下面两行是用来去除回车符的
                        #与最下面处理p标签的分支具有相同的功能
                        #求大神指导一下QAQ
                        r_content = tbs.get_text()
                        r_content = re.match(r'.*?$', r_content)
                        md_file.write(r_content.group())
                md_file.write('  \n')

            # h1~h6，最省心标签
            elif re.search('<h1+', str(content)):
                md_file.write('#' + content.get_text() + '  \n')
            elif re.search('<h2+', str(content)):
                md_file.write('##' + content.get_text() + '  \n')
            elif re.search('<h3+', str(content)):
                md_file.write('###' + content.get_text() + '  \n')
            elif re.search('<h4+', str(content)):
                md_file.write('####' + content.get_text() + '  \n')
            elif re.search('<h5+', str(content)):
                md_file.write('#####' + content.get_text() + '  \n')
            elif re.search('<h6+', str(content)):
                md_file.write('######' + content.get_text() + '  \n')

            # p标签，随意写就好
            elif re.search('<p>.*?', str(content)):
                r_content = content.get_text()
                #这里利用了正则匹配符$的“只到结尾或回车符之前”的特性，屏蔽了结尾的换行
                r_content = re.match(r'.*?$', r_content)
                md_file.write(r_content.group() + '  \n')

            # print(content)
        md_file.close()

if __name__ == "__main__":
    translator = Translator()
    #这个Url指向一个百合老番的女主的简介页面，可以改成别的。
    url = "https://zh.moegirl.org/%E5%A8%9C%E8%92%82"
    sources = translator.find_we_need(url)
    translator.translate(sources)