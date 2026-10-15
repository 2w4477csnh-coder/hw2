n=int(input())
if n==1:
    print(0)
elif n<=10:
    print(n-1)
elif n<=190:
    n=n-11
    a=n//2+10
    if n%2==0:
        print(a//10)
    else:
        print(a%10)
else:
    n=n-191
    a=100+n//3
    if n%3==0:
        print(a//100)
    elif n%3==1:
        print(a//10%10)
    else:
        print(a%10)





