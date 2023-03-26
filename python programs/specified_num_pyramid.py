s=int(input())
n=int(input())
for i in range(1,n+1):
    a=""
    for j in range(1,i+1):
        a=a+str(s)+" "
        s=s+1
    print(a)