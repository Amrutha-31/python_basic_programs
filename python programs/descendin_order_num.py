n=int(input())
a=""
for i in range(1,n+1):
    a=""
    for j in range(1,n+1):
        a=a+str(j)+" "
    print(a)
    n=n-1