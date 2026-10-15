k=input()
if int(k[1])%2!=0 and (k[0]=='a' or k[0]=='c' or k[0]=='e' or k[0]=='g'):
    print('черный')
elif int(k[1])%2==0 and (k[0]=='b' or k[0]=='d' or k[0]=='f' or k[0]=='h'):
    print('черный')
else:
    print('белый')
