lyrics  =  """ Kayar jo the, vo shayar bane
Ab kya kya karein ye ishq mein
Na kehte the kuch jo, lage khoj mein
Kya lafz chune? Naye aashiq ye,
ishq mein tere hain faiz bane
Arz kiya hai
Humne bhi likha kuch tere baare mein
Aise tu lage ki gulaab hai
Aur aise tu lage ki gulaab hai
Baghon mein dil ke
Khilke in fizaaon mein chhaye ho haaye
Aur vaise hum to tere hi gulaam hain
Aur vaise hum to tere hi gulaam hain
Baadshah dil ke, teri baazi mein
Jo tu chahe to…
Doobe dilon ki kya nau banu?
Main khud tar paaoon na aankhon mein
Shayar ki fitrat mein hi doobna
Main kya hi ladu toofanon se
Ishq mein tere hain faiz bane
Arz kiya hai
Humne bhi likha kuch tere baare mein
Haathon ko sambhaale mere haathon mein
Kaise haathon ko sambhaale mere haathon mein?
Jab tak neend na aaye in lakeeron mein
Baatein hon…
Haan… """


import turtle
import time
import colorsys
import playsound
import sys
import pyautogui
playsound.playsound("Arz Kiya Hai(KoshalWorld.Com).mp3", False)
time.sleep(38.8)
pyautogui.click(1362,1170)
# time.sleep(1)
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Typing Effect with Turtle")
t = turtle.Turtle()
t.hideturtle()
t.goto(50,300)
t.pencolor("yellow")
t.speed(0)
t.write("Now Playing:Arz kiya hai", font=("courier", 20, "underline","bold"),align='right')
t.speed(3)
t.penup()
h = 0
timeset = [3.9,1.5,1,1.3,1.1,0.1,0.4,0.5,0.1,1.5,3.5,1,1,0.5,3.3,0.3,1.5,0.9,1.8,0.9,0.5,0.2,0.1,0.2,1,0.9,0.7]
k=15
g=0
def typing_effect_duration(text,duration):
    z=[0,0,-20,0,-9,70,-40,-10,20,30,24,36,-40,0,10,-10,20,-10,0,20,70,-5,-20,-40,-30,70,100]
    n = len(text)  
    if n == 0:
        return
    h = 0
    global k,g
    t.goto(-250+z[g],250-k)
    g+=1
    k=k+30
    for char in text:
        #  sys.stdout.write(char)
        #  sys.stdout.flush()
        t.pencolor("#00ff85")
        t.write(char, font=("courier", 20, "italic"),align='left')
        t.forward(15)
        time.sleep(0.06)
    # print()
i = 0
for lines in lyrics.splitlines():
    #  t.clear()
        if(i==18):
            t.clear()
            k=50
            t.goto(50,300)
            t.pencolor("yellow")
            t.speed(0)
            t.write("Now Playing:Arz kiya hai", font=("courier", 20, "underline","bold"),align='right')
            t.speed(3)
            t.penup()
            
        typing_effect_duration(lines, 3)
        time.sleep(timeset[i])
        i = i + 1
turtle.tracer(0)
t.pensize(2)
t.goto(-280,-280)
t.pencolor(colorsys.hsv_to_rgb(h,1,1))
def draw_heart(size):
    t.left(140)
    t.begin_fill()
    
    # Left curve
    t.forward(size)
    for i in range(200):
        t.right(1)
        t.forward(size * 0.009)
    
    t.left(120)
    
    for i in range(200):
        t.right(1)
        t.forward(size * 0.009)
    
    t.forward(size)
    t.end_fill()
    t.setheading(0)

size = 180 - (10 * 15)
h+=0.05
draw_heart(size)
t.penup()
t.pencolor(colorsys.hsv_to_rgb(h,1,1))
h+=0.05
t.goto(-250,-290)
t.pendown()
draw_heart(size)
t.penup()
t.goto(-250,-300)
t.pendown()
t.pencolor(colorsys.hsv_to_rgb(h,1,1))
h+=0.05
draw_heart(size)
t.penup()
t.goto(250,230)
t.pendown()
def draw_heart(size):
   
    t.left(140)
    t.begin_fill()
    
    # Left curve
    t.forward(size)
    for i in range(200):
        t.right(1)
        t.forward(size * 0.009)
    
    t.left(120)
    
    for i in range(200):
        t.right(1)
        t.forward(size * 0.009)
    
    t.forward(size)
    t.end_fill()
    t.setheading(0)
h=0
size = 180 - (8 * 15)
t.pencolor(colorsys.hsv_to_rgb(h,1,1))
h+=0.05
draw_heart(size)
t.penup()
t.goto(280,240)
t.pendown()
t.pencolor(colorsys.hsv_to_rgb(h,1,1))
h+=0.05
draw_heart(size)
t.penup()
t.goto(280,250)
t.pendown()
h+=0.05
t.pencolor(colorsys.hsv_to_rgb(h,1,1))
draw_heart(size)
time.sleep(5)
turtle.done()
sys.exit()
