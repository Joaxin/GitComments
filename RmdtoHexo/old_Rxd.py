from bs4 import BeautifulSoup
import re
import os
path = os.getcwd()
flist = os.listdir(path)

for fl in flist:
    fhtml = re.search(r'.*?(\.html)$',fl)
    if fhtml:
        print("正在处理 " + fhtml.group())
        with open(path + '/' + fl,'rb') as fp:
            soup_pre = fp.read().decode('utf-8')
            formatter = re.search('(---.*?---)',soup_pre, re.S).group(1)
            if formatter:
                soup_pre = re.sub('(---.*?---)','',soup_pre,flags = re.S)
            
            soup = BeautifulSoup(soup_pre,"lxml")
            [x.extract() for x in soup.head.find_all('script')]
            [x.extract() for x in soup.head.find_all('style')]
            [x.extract() for x in soup.head.find_all('meta')]
            [x.extract() for x in soup.head.find_all('link')]
            if soup.header:
                soup.header.extract()
            if soup.select(".page-header"):
                soup.select(".page-header")[0].extract()

            code = soup.select("div.sourceCode")
            print("截获到" + str(len(code)) + "个代码片段\n")
            wrapper1 = '<div class="code-area-wrap"><div class="highlight-tools"><i class="fa fa-angle-down code-expand" aria-hidden="true"></i><div class="code_lang">R</div><div class="copy-notice"></div><i class="fa fa-clipboard" aria-hidden="true"></i></div><figure class="highlight R"><table><tbody><tr><td class="code">'
            wrapper2 = '</tr></tbody></table></figure></div>'
            for cd in soup.select("div.sourceCode"):
                cc = cd.code
                cc.name = "pre"
                ccc = wrapper1 + str(cc) + wrapper2
                cd.replace_with(BeautifulSoup(ccc,"html.parser"))


            ## Repalce <pre><code>
            codeTag = soup.select("pre>code")
            wrapper3 = '<div class="code-area-wrap"><div class="highlight-tools"><i class="fa fa-angle-down code-expand" aria-hidden="true"></i><div class="code_lang">R</div><div class="copy-notice"></div><i class="fa fa-clipboard" aria-hidden="true"></i></div><figure class="highlight OUTPUT"><table><tbody><tr><td class="code">'
            print("截获到" + str(len(codeTag)) + "个未知代码片段\n")
            for cd in soup.select("pre>code"):
                cd.parent.unwrap()
                cc = cd
                cc.name = "pre"
                ccc = wrapper3 + str(cc) + wrapper2
                cd.replace_with(BeautifulSoup(ccc,"html.parser"))
            
            pattern = {"\"co\"": "\"comment\"",
                    "\"kw\"": "\"keyword\"",
                    "\"st\"": "\"string\"",
                    "\"dv\"": "\"number\"",
                    "\"op\"": "\"string\""
                
            }
            for pat in pattern:
                soup = re.sub(pat,pattern[pat],str(soup))
        with open(path + '/' +  fl,'wb') as fp:
            soup_after = formatter + '\n' + str(soup)
            fp.write(soup_after.encode('utf-8'))



