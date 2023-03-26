n=int(input())
count=0
for i in range(1,n+1):
    a=i
    b=n-i
    if a<b and a+b==n:
        count=count+1
print(count)