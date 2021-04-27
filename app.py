import turtle
from random import randint
from time import sleep
score = 0
high_score = 0
delay = 0.10
#configuracion ventana
ventana = turtle.Screen()
ventana.title("Snake Python M.A.M.S")
ventana.bgcolor("black")
ventana.setup(width=300,height=300)

#texto
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,280)
texto.write('Puntos  0  Puntaje total 0', align="center", font=("Ubuntu", 20, 'normal'))
#CONFIG TURTLE
head = turtle.Turtle()
head.speed(0)
head.color('white')
head.shape('square')
head.penup()
head.goto(0,0)
head.direction = 'stop'

#body new
body_now = []

#food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(50,60)

def ariba():
    head.direction = 'up'

def abajo():
    head.direction = 'down'

def izq():
    head.direction = 'left'


def der():
    head.direction = 'right'



def mover():
    if head.direction =='up':
        y = head.ycor()
        head.sety(y + 20)

    elif head.direction == 'down':
        y = head.ycor()
        head.sety(y - 20)
        

    elif head.direction == 'left':
        x = head.xcor()
        head.setx(x - 20)
        
    elif head.direction == 'right':
        x = head.xcor()
        head.setx(x + 20)


#keyboard
ventana.listen()
ventana.onkey(ariba,'Up')
ventana.onkey(abajo,'Down')
ventana.onkey(izq,'Left')
ventana.onkey(der,'Right')

while True:
    ventana.update()
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        head.goto(0,0)
        head.direction = 'stop'

        for body in body_now:
            body.goto(4000,4000)

    if head.distance(food) < 20:
        x = randint(-280,280)
        y = randint(-280,280)
        food.goto(x,y)

        body_new = turtle.Turtle()
        body_new.speed(0)
        body_new.color('white')
        body_new.shape('square')
        body_new.penup()
        body_now.append(body_new)

        score += 10 
        if score > high_score:
            high_score = score

        texto.clear()
        texto.write("Puntos {}  Puntaje maxinmo {}".format(score,high_score),align="center", font=("Ubuntu", 20, 'normal'))
    
    body_total = len(body_now)
    for index in range(body_total - 1, 0, -1):
        x = body_now[index-1].xcor()
        y = body_now[index-1].ycor()
        body_now[index].goto(x,y)
    
    if body_total > 0:
        x= head.xcor()
        y = head.ycor()
        body_now[0].goto(x,y)
    sleep(delay)
        





    mover()


turtle.mainloop()