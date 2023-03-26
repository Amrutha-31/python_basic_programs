n=int(input())
b=1
for i in range(1,n+1):
    a=""
    for j in range(1,i+1):
        a=a+str(b)+" "
        b=b+1
    print(a)