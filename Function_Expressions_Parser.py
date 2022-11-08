import turtle
from math import *

expression = str(input('Enter the function expression：（e.g. y=114514*x+1919810）'))#输入表达式

x = -500
try:
    exec(expression)
except:
    print('Error!')
    input()
    exit()

p = turtle.Turtle()#初始化
p.speed('fastest')

###########
#构建坐标轴
p.up()
p.goto(-500,0)
p.down()
p.forward(500*2)#画出横坐标轴
#画箭头
#横
p.left(135)#上半
p.forward(50)
p.backward(50)
p.right(135)
p.right(135)#下半
p.forward(50)
p.backward(50)
p.left(135)
#竖
p.backward(500)
p.left(90)
p.forward(500)
p.backward(500*2)
p.forward(500*2)
p.left(135)#左半
p.forward(50)
p.backward(50)
p.right(135)
p.right(135)#右半
p.forward(50)
p.backward(50)
p.left(135)
###########

p.up()
p.goto(x,y)
p.color('red')
p.down()

while True:
    try:
        exec(expression)
    except:
        pass
    x = x + 1
    p.goto(x,y)
