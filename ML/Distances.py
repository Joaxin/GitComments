from numpy import *

vector1 = mat([1, 2, 3])
vector2 = mat([4, 5, 6])
print(sqrt((vector1 - vector2) * ((vector1 - vector2).T)))
print(sum(abs(vector1-vector2)))
print(abs(vector1 - vector2).max())
print(dot(vector1,vector2)/(linalg.norm(vector1)*linalg.norm(vector2)))
matV = mat([[1,1,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,1,1]])
smstr = nonzero(matV[0]-matV[1]);
print(shape(smstr[0])[1])
import scipy.spatial.distance as dist  # 导入scipy距离公式
matV = mat([[1,1,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,1,1]])
print("dist.jaccard:", dist.pdist(matV, 'jaccard'))