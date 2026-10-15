h=input()
n, m = h.split('-')
x1=ord(n[0])
y1=int(n[1])
x2=ord(m[0])
y2=int(m[1])
r=abs(x1-x2)
s=abs(y1-y2)
if (s==2 and r==1) or (s==1 and r==2):
    print('верно')
else:
    print('ошибка')