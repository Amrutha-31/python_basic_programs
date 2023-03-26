import numpy as np
x=np.array([[1,2,3],[4,5,6],[7,8,9]])
y=np.array([[9,8,7],[6,5,4],[3,2,1]])
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(y)):
        for k in range(len(y)):
            result[i][j]+=x[i][k]*y[k][j]
for r in result:
    print(r)