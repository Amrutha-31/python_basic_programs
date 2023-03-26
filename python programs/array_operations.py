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
print("array:",mat)
a=0
for i in mat:
    for j in i:
        a=a+j
print("sum of all elements in an array:",a)
b=1
for i in mat:
    for j in i:
        if j==0:
            continue
        else:
            b=b*j
print("product of all elements in an array:",b)
total=0
for i in range(len(mat)):
    total=total+mat[i][i]
print("sum of diagonal elements are:",total)
total1=1
for i in range(len(mat)):
    total1=total1*mat[i][i]
print("product of diagonal elements are:",total1)