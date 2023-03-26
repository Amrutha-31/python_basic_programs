n=int(input())
Factors=0
for i in range(2,n):
    if n%i==0:
        Factors=Factors+1
if Factors==0:
    print("Prime Number")
else:
    print("Not a Prime Number")