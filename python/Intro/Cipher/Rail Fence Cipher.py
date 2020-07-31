#!/usr/bin/env python
# -*- coding: utf_ -*-

cipher = "teeibbhkysio"
length = len(cipher)
field = []
for i in range(2, length):
    if length % i == 0:
        field.append(i)
for Fence in field:
    qu = length // Fence
    result = {x: cipher[qu * x:qu * x+ qu:] for x in range(Fence)}
    answer = []
    for i in range(qu):
        for j in range(Fence):
            answer.append(result[j][i])
    # print(result)
    print('\t'+str(Fence)+'\t'+'Fence '+"".join(answer))
