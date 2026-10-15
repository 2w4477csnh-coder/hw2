import turtle
xc=float(input('xc = '))
yc=float(input('yc = '))
r=float(input('r = '))
x=float(input('x = '))
y=float(input('y = '))
e=(xc-x)**2+(yc-y)**2
if e>r**2:
    m='точка вне окружности'
elif e==r**2:
    m='точка на окружности'
else:
    m='точка внутри окружности'
t=turtle.Turtle()
t.shape("turtle")
t.speed(0)
t.up()
t.goto(xc,yc-r)
t.down()
t.circle(r)
t.up()
t.goto(x,y)
t.dot(10,'red')
t.up()
t.goto(xc-40,yc-r-20)
t.color('red')
t.write(m)
t.hideturtle()
turtle.done()