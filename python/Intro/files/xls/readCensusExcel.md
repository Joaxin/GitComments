假定你有一张电子表格的数据，来自于 2010 年美国人口普查。你有一个无聊的任务，要遍历表中的几千行，计算总的人口，以及每个县的普查区的数目（普查区就是一个地理区域，是为人口普查而定义的）。每行表示一个人口普查区。
尽管 Excel 是要能够计算多个选中单元格的和，你仍然需要选中 3000 个以上县的单元格。即使手工计算一个县的人口只需要几秒钟，整张电子表格也需要几个小时时间。 

在这个项目中，你要编写一个脚本，从人口普查电子表格文件中读取数据，并
在几秒钟内计算出每个县的统计值。 
下面是程序要做的事： 
•    从 Excel 电子表格中读取数据。 
•    计算每个县中普查区的数目。 
•    计算每个县的总人口。 
•    打印结果。 
这意味着代码需要完成下列任务： 
•    用 openpyxl 模块打开 Excel 文档并读取单元格。 
•    计算所有普查区和人口数据，将它保存到一个数据结构中。 
•    利用 pprint 模块，将该数据结构写入一个扩展名为.py 的文本文件。

censuspopdata.xlsx 电子表格中只有一张表，名为'Population by Census Tract'。每
一行都保存了一个普查区的数据。列分别是普查区的编号（A），州的简称（B），县
的名称（C），普查区的人口（D）。 
打开一个新的文件编辑器窗口，输入以下代码。将文件保存为readCensusExcel.py。 

```python
>>> import os 
>>> os.chdir('C:\\Python34') 
>>> import census2010 
>>> census2010.allData['AK']['Anchorage'] 
{'pop': 291826, 'tracts': 55} 
>>> anchoragePop = census2010.allData['AK']['Anchorage']['pop'] 
>>> print('The 2010 population of Anchorage was ' + str(anchoragePop)) 
The 2010 population of Anchorage was 291826 
```





