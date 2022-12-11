import turtle
tao=turtle.Pen()
tao.shape('turtle')
def Warif () :
    for i in range (11):
        tao.color('red')
        tao.circle(100)
        tao.left(40)
        tao.color('green')
        tao.circle(80)
        tao.left(35)
        tao.color('blue')
        tao.circle(60)
        tao.left(30)
        tao.color('yellow')
        tao.circle(40)
        tao.left(25)
def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()
   
        

Warif()
Go(200,200)
for i in range (2):
    tao.color('blue')
    tao.foward(150)
    tao.left(150)
print(i)
