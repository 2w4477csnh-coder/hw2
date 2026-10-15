n, k, m = map(int,input().split())
r=n*2
s=r//k
if r%k!=0:
    s=s+1
t=s*m
print(t)

