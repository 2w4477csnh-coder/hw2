n,k,m=map(int,input().split())
p1=abs(k-m)
p2=n-p1
if p1>p2:
    print(p2-1)
else:
    print(p1-1)
