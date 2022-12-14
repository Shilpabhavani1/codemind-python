import math
n=int(input())
s=0
arr=list(map(int,input().split()))
for i in arr:
    d=math.sqrt(i)
    if(i*i%d==0):
        s=s+i
print(s)