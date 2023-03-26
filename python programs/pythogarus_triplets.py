n=int(input())
count=0
for i in range(1,n+1):
    for j in range(2,n+1):
        for m in range(3,n+1):
            a=i
            b=j
            c=m
            if ((a**2)+(b**2)==(c**2)) and (a<b) and (b<c):
                count=count+1
print(count)