m=int(input())
n=int(input())
a=""
b=1
for i in range(1,m+1):
    a=""
    for j in range(1,n+1):
        a=a+str(b)+" "
        b=b+1
    print(a)