n=int(input())
arr=list(map(int,input().split()))
for i in arr:
    d=arr.count(i)
    if d>=2:
        print(i)
        break