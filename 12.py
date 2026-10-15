a=int(input())
if 11<=a%100<=14:
    print(a, 'попугаев')
elif a%10==1:
    print(a,'попугай')
elif a%10==2 or a%10==3 or a%10==4:
    print(a,'попугая')
else:
    print(a,'попугаев')