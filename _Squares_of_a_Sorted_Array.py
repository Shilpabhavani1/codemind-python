n=int(input())
arr=list(map(int,input().split()))
s=[]
for i in arr:
    v=i*i
    s.append(v)
s.sort()
print(*s)
    