n=int(input())
for i in range(1,n+1):
    a=""
    for j in range(i):
        a=a+str(j+1)+" "
        b=""
        for m in range(1,i):
            b=b+str(m)+" "
    print(a+b)