import webbrowser, sys 
if len(sys.argv) > 1: 
    ## sys.argv 变量保存了程序的文件名和命令行参数的列表，这里去掉程序的名称
    address = ' '.join(sys.argv[1:]) 
    print(sys.argv)
else: 
    ## 处理剪贴板内容，从剪切板得到信息 
    address = pyperclip.paste() 
 
webbrowser.open('https://www.google.com/maps/place/' + address) 