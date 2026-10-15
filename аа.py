a=input('Возраст Антона:')
b=input('Возраст Бориса:')
c=input('Возраст Виктора:')
if a>b and a>c:
    print('Антон старше всех')
if b>a and b>c:
    print('Борис старше всех')
if c>b and c>a:
    print('Виктор старше всех')
if a==b and a>c and b>c:
    print('Борис и Антон старше Виктора')
if b==c and b>a and c>a:
    print('Борис и Виктор старше Антона')
if a==c and a>b and c>b:
    print('Антон и Виктор старше Бориса')
