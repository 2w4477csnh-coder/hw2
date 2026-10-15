a,b=map(int,input().split('x'))
c,d,e=map(int,input().split('x'))
if (c<=b and d<=a) or (c<=a and d<=b):
    print('да')
elif (c<=b and e<=a) or (c<=a and e<=b):
    print('да')
elif (d<=b and e<=a) or (d<=a and e<=b):
    print('да')
else:
    print('нет')
