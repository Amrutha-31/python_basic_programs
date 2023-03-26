import numpy
x=int(input("enter no.of rows:"))
y=int(input("enter no.of columns:"))
mat=[]
for i in range(0,x):
    mat.append([])
for i in range(0,x):
    for j in range(0,y):
        mat[i].append(j)
        mat[i][j]=0
for i in range(0,x):
    for j in range(0,y):
        print("enter no.of row:",i+1,"col:",j+1)
        mat[i][j]=int(input())
print(mat)
a=0
for i in mat:
    for j in i:
        a=a+j
print(a)