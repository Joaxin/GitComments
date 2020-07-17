__author__ = 'root'
import math
from math import sqrt

def length(a,b):   #计算两个对象之间的欧式距离
    sum=0
    for i in range(0,a.__len__()):
        sum=sum+(a[i]-b[i])*(a[i]-b[i])
    sum=math.sqrt(sum)
    return sum

def similarity(subjects):    #计算类与类之间的相似度
    simi=[[0 for col in range(0,subjects.__len__(),1)]for row in range(0,subjects.__len__(),1)]
    for i in range(0,subjects.__len__()):
        for j in range(i+1,subjects.__len__()):
            simi[i][j]=simi[j][i]=length(subjects[i],subjects[j])
    return simi




def distances(a,b,similar):  #用最近邻方法计算新类与旧类之间的相似度
    for i in range(0,len(similar)):
        similar[a][i]=similar[i][a]=min(similar[a][i],similar[b][i])
    del similar[b]
    for i in range(0,len(similar)):
        del similar[i][b]
    return similar


def clustering(subjects,similar):   #聚类函数
    clusters=[[0 for col in range(0,len(subjects))]for row in range(0,len(subjects))]   #初始化n个类
    for i in range(0,len(subjects)):
        clusters[i]=[i]

    while len(clusters)>1:    #判断聚类是否完成
        distance=100
        point1=0
        point2=0
        for i in range(0,len(similar)):
            for j in range(i+1,len(similar)):
                if similar[i][j]==0:
                    continue
                elif similar[i][j]<distance:
                    distance=similar[i][j]
                    point1=i
                    point2=j
        similar=distances(point1,point2,similar)
        clusters[point1].append(clusters[point2])    #合成距离最小的两个类
        del clusters[point2]   #类的总数减少了一个

    return clusters



subjects=[[0.0, 0.8, 0.0, 0.4, 0.7, 0.7, 0.1, 0.0],
          [0.5, 0.8, 1.0, 0.0, 0.5, 0.9, 0.7, 0.2],
          [0.1, 0.2, 0.5, 0.4, 0.6, 0.7, 0.7, 0.8],
          [0.6, 0.5, 1.0, 0.9, 0.9, 0.4, 0.2, 0.5],
          [0.5, 0.5, 1.0, 1.0, 0.0, 1.0, 0.9, 0.5],
          [0.0, 0.4, 1.0, 0.9, 0.9, 0.3, 0.3, 0.8],
          [0.4, 0.8, 0.2, 0.2, 0.0, 0.8, 0.0, 0.3],
          [0.2, 0.3, 0.9, 0.3, 0.3, 0.9, 0.1, 0.1],
          [0.4, 0.6, 0.4, 0.0, 0.7, 0.3, 0.0, 0.0],
          [0.7, 1.0, 0.6, 0.9, 0.1, 0.0, 1.0, 0.2]]

similar=similarity(subjects)

clusters=clustering(subjects,similar)
print(clusters)
