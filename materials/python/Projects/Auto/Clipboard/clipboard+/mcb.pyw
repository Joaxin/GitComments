#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
'''
假定你有一个无聊的任务，要填充一个网页或软件中的许多表格，其中包含一
些文本字段。剪贴板让你不必一次又一次输入同样的文本，但剪贴板上一次只有一
个内容。如果你有几段不同的文本需要拷贝粘贴，就不得不一次又一次的标记和拷
贝几个同样的内容。 
可以编写一个 Python 程序，追踪几段文本。这个“多重剪贴板”将被命名为
mcb.pyw（因为“mcb”比输入“multiclipboard”更简单）。.pyw 扩展名意味着 Python
运行该程序时，不会显示终端窗口（详细内容请参考附录 B）。 
该程序将利用一个关键字保存每段剪贴板文本。例如，当运行 py mcb.pyw save 
spam，剪贴板中当前的内容就用关键字 spam 保存。通过运行 py mcb.pyw spam，这
段文本稍后将重新加载到剪贴板中。如果用户忘记了都有哪些关键字，他们可以运
行 py mcb.pyw list，将所有关键字的列表复制到剪贴板中。 
下面是程序要做的事： 
•    针对要检查的关键字，提供命令行参数。 
•    如果参数是 save，那么将剪贴板的内容保存到关键字。 
•    如果参数是 list，就将所有的关键字拷贝到剪贴板。 
•    否则，就将关键词对应的文本拷贝到剪贴板。 
这意味着代码需要做下列事情： 
•    从 sys.argv 读取命令行参数。 
•    读写剪贴板。 
•    保存并加载 shelf 文件。 
'''

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        print(sys.argv[2] + ":" + pyperclip.paste() + "| Saved.")
elif len(sys.argv) == 2:
# List keywords and load content.
    if sys.argv[1].lower() == 'list':
        print(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(sys.argv[1] + ":" + mcbShelf[sys.argv[1]] + "| Copied.")

mcbShelf.close()
