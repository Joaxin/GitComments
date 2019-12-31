> Rmd HTML转  Hexo
>
> 仅适用于Butterfly主题

### Hexo代码高亮

```python
<div class="code-area-wrap"><i class="fa fa-angle-down code-expand" aria-hidden="true"></i>
    <div class="copy-notice"></div><i class="fa fa-clipboard" aria-hidden="true"></i>
    <div class="code_lang">python</div>
    <figure class="highlight python">
        <table>
            <tbody>
                <tr>
                    <td class="gutter">
                        <pre><span class="line">1</span><br><span class="line">2</span><br><span class="line">3</span><br><span class="line">4</span><br><span class="line">5</span><br><span class="line">6</span><br></pre>
                    </td>
                    <td class="code">
                        <pre>
                        <span class="line"><span class="keyword">import</span> logging</span><br>
                        <span class="line">logging.captureWarnings(<span class="literal">True</span>)</span><br>
                        
                        <span class="line">response = R.get(<span class="string">'https://www.12306.cn'</span>, verify=<span class="literal">False</span>)</span><br>
                        <span class="line"><span class="comment"># response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))</span></span><br>
                        <span class="line">print(response.status_code)</span><br>
                        
                        <span class="line"><span class="comment"># 200</span></span><br>
                        </pre>
                    </td>
                </tr>
            </tbody>
        </table>
    </figure>
</div>
```

Butterfy 2.x 对修改了部分代码高亮代码，其中，

```html
<i class="fa fa-angle-down code-expand" aria-hidden="true"></i>
    <div class="copy-notice"></div><i class="fa fa-clipboard" aria-hidden="true"></i>
    <div class="code_lang">python</div>
```

改为

```html
<div class="highlight-tools">
    <i class="fa fa-angle-down code-expand" aria-hidden="true"></i>	   <div class="code_lang">python</div>
    <div class="copy-notice"></div><i class="fa fa-clipboard" aria-hidden="true"></i>
</div>
```

所以对于V1.x 请使用脚本`old_Rxd.py`, 对于最新版请使用`Rxd.py`

### Rmd生产的代码

```html
<div class="sourceCode"><pre class="sourceCode r"><code class="sourceCode r">1i<span class="op">*</span>(<span class="dv">9</span><span class="op">:</span><span class="dv">1</span>)
<span class="co"># 0+9i 0+8i 0+7i 0+6i 0+5i 0+4i 0+3i 0+2i 0+1i</span>
<span class="kw">Re</span>(<span class="dv">1</span> <span class="op">+</span><span class="st"> </span>2i);<span class="kw">Im</span>(<span class="dv">1</span> <span class="op">+</span><span class="st"> </span>2i)
<span class="co"># 1</span>
<span class="co"># 2</span>
<span class="kw">Mod</span>(<span class="dv">1</span> <span class="op">+</span><span class="st"> </span>2i)
<span class="co"># 2.236068</span>
<span class="kw">Arg</span>(<span class="dv">1</span> <span class="op">+</span><span class="st"> </span>2i)
<span class="co"># 1.107149</span>
<span class="kw">Conj</span>(<span class="dv">1</span> <span class="op">+</span><span class="st"> </span>2i)
<span class="co"># 1-2i</span></code></pre></div>
```

### 思路

1. 包裹

```html
<div class="code-area-wrap"><i class="fa fa-angle-down code-expand" aria-hidden="true"></i>
    <div class="copy-notice"></div><i class="fa fa-clipboard" aria-hidden="true"></i>
    <div class="code_lang">R</div>
    <figure class="highlight R">
        <table>
            <tbody>
                <tr>
                ....
                </tr>
            </tbody>
        </table>
    </figure>
</div>
```

2. 外壳变换

```html
<div class="sourceCode">
	<pre class="sourceCode r">
		<code class="sourceCode r">
		</code>
	</pre>
</div>
```

==>

```html
<td class="code">
	<pre>...</pre>
</td>
```

3. 关键词替换

```
"co" ==> "comment"
"kw" ==> "keyword"
"st" ==> "string"
"dv" ==> "number"
"op" ==> "string"
```

4. 去掉前置空格

去掉

```html
<title>R Introduction</title>
<!--去掉-->
</head>
<!--去掉-->
<header>
<div class="inner">
<h1 class="title toc-ignore">R Introduction</h1>
<h3 class="author">Joaxin</h3>
<h3 class="date">2018-06-15</h3>
</div>
</header>
```

5. 添加Formatter

```yaml
---
title: 
date: 
updated:
tags:
categories:
toc:
cover:
description:
---
```

6. 完整代码

	> 其他更新详见.py脚本

 ```python
from bs4 import BeautifulSoup
import re
with open("R_intro_out.html", "w+", encoding='utf-8') as fp:
    soup = BeautifulSoup(open('R_intro.html'),"lxml")
    [x.extract() for x in soup.head.find_all('script')]
    [x.extract() for x in soup.head.find_all('style')]
    [x.extract() for x in soup.head.find_all('meta')]
    [x.extract() for x in soup.head.find_all('link')]
    soup.header.extract()
    
    code = soup.select("div.sourceCode")
    print("截获到" + str(len(code)) + "个代码片段\n")
    wrapper1 = '<div class="code-area-wrap"><i class="fa fa-angle-down code-expand" aria-hidden="true"></i><div class="copy-notice"></div><i class="fa fa-clipboard" aria-hidden="true"></i><div class="code_lang">R</div><figure class="highlight R"><table><tbody><tr><td class="code">'
    wrapper2 = '</tr></tbody></table></figure></div>'
    for cd in soup.select("div.sourceCode"):
        cc = cd.code
        cc.name = "pre"
        ccc = wrapper1 + str(cc) + wrapper2
        cd.replace_with(BeautifulSoup(ccc))
    
    pattern = {"\"co\"": "\"comment\"",
               "\"kw\"": "\"keyword\"",
               "\"st\"": "\"string\"",
               "\"dv\"": "\"number\"",
               "\"op\"": "\"string\""
        
    }
    for pat in pattern:
        soup = re.sub(pat,pattern[pat],str(soup))
    fp.write(str(soup))
 ```

```Output
	正在处理 bioc_ChIPseeker.html
	截获到35个代码片段
	
	正在处理 Bioc_emojifont.html
	截获到27个代码片段
	
	正在处理 Bioc_ggtree.html
	截获到80个代码片段
	
	正在处理 Bioc_Ranges.html
	截获到66个代码片段
	
	正在处理 ggplot2_intro.html
	截获到48个代码片段
	
	正在处理 ggplot2_theme.html
	截获到59个代码片段
	
	正在处理 ggplot2_usborn.html
	截获到19个代码片段
	
	正在处理 R_adv.html
	截获到22个代码片段
	
	正在处理 R_anova.html
	截获到7个代码片段
	
	正在处理 R_corrlation.html
	截获到11个代码片段
```

