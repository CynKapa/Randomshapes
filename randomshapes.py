import turtle
import random
t=turtle.Turtle()
t.speed(15)
colours=['Black','White',
         'Red',
         'Lime',
         'Blue',
         'Yellow',
         'Cyan',
         'Magenta',
         'Silver',
         'Gray',
         'Maroon',
         'Olive',
         'Green',
         'Purple',
         'Teal',
         'Navy'
,
         'maroon',
         'dark red',
         'brown',
         'firebrick',
         'crimson',
         'red',
         'tomato',
         'coral',
         'indian red',
         'light coral',
         'dark salmon',
         'salmon',
         'light salmon',
         'orange red',
         'dark orange',
         'orange',
         'gold',
         'yellow green',
         'dark olive green',
         'olive drab',
         'lawn green',
         'green yellow',
         'forest green',
         'lime',
         'light green',
         'pale green',
         'dark sea green',
         'medium sea green',
         'dark slate gray',
         'teal',
         'dark cyan',
         'dark turquoise',
         'deep sky blue',
         'dodger blue',
         'light blue',
         'sky blue',
         'light sky blue',
         'midnight blue',
         'navy',
         'dark blue',
         'medium blue',]
mic=random.randint(15,60)
class Shapes():
    def __init__(self,x,y,len):
        self.x=x
        self.y=y
        self.len=len

    def square(self):
        t.pu()
        t.goto(self.x,self.y)
        t.color(colours[1].lower())
        t.begin_fill()
        for i in range (1,5):
            t.pendown()
            t.fd(self.len)
            t.rt(90)
        t.end_fill()
        t.penup()
        random.shuffle(colours)
    def longsquare(self):
        global mic
        t.pu()
        t.goto(self.x, self.y)
        t.color(colours[1].lower())
        t.begin_fill()
        for i in range(0, 2):
            t.pendown()
            t.rt(90)
            t.fd(mic)
            t.rt(90)
            t.fd(self.len)
        t.end_fill()
        t.penup()
        random.shuffle(colours)
    def triangle(self):
        t.pu()
        t.goto(self.x, self.y)
        t.color(colours[1].lower())
        t.begin_fill()
        for i in range (0,3):
            t.pendown()
            t.fd(self.len)
            t.rt(120)
        t.end_fill()
        random.shuffle(colours)
    def circle(self):
        t.pu()
        t.goto(self.x, self.y)
        t.color(colours[1].lower())
        t.begin_fill()
        t.pendown()
        t.circle(self.len)
        t.end_fill()
        random.shuffle(colours)


for i in range(0,70):
    a=random.randint(1,4)
    if a==1 :
        cynthia=Shapes(x=random.randint(-300,300),y=random.randint(-300,300),len=random.randint(5,50))
        cynthia.square()
    if a==2:
        cynthia = Shapes(x=random.randint(-300, 300), y=random.randint(-300, 300), len=random.randint(0, 100))
        cynthia.circle()
    if a==3:
        cynthia = Shapes(x=random.randint(-300, 300), y=random.randint(-300, 300), len=random.randint(0, 100))
        cynthia.triangle()
    if a==4:
        cynthia = Shapes(x=random.randint(-300, 300), y=random.randint(-300, 300), len=random.randint(0, 100))
        cynthia.longsquare()
turtle.done()

