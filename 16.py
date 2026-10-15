n=input()
if len(n)==4 and len(set(n))==4 and not(1900<=int(n)<=2050):
    print('OK')
else:
    print('ERROR')


