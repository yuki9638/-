import pyxel

pyxel.init(200,200)
pyxel.mouse(True)
class Ball :
  speed=1
  def __init__(self):
   self.angle = pyxel.rndi(30,150)
   self.ballx= pyxel.rndi(0,199)
   self.bally = 0
   self.vx = pyxel.cos(self.angle)
   self.vy = pyxel.sin(self.angle)
  def move(self):
    for i in range (len(ball)) :
     ball[i].ballx += ball[i].vx
     ball[i].bally += ball[i].vy
ball =[Ball()]
class Padx :
  def __init__(self):
   self.padx = pyxel.mouse_x
padx=Padx()
score = 0
pyxel.sound(0).set("e0e1c1","p","3","s",10)

pyxel.sound(1).set("a2c3","t","7","v",50)
error=0
s=1
def update():
    global score,angle,error,s,speed
    padx.padx = pyxel.mouse_x
    for i in range (len(ball)) :
     ball[i].ballx += ball[i].vx
     ball[i].bally += ball[i].vy
     if ball[i].bally >= 196:
        ball[i].ballx = pyxel.rndi(0,199)
        ball[i].bally = 0
        ball[i].vx=ball[i].vx*ball[i].speed
        ball[i].vy=ball[i].vy*ball[i].speed
     if ball[i].ballx >=200 :
        ball[i].vx=-ball[i].vx
     if ball[i].ballx<=0 :
        ball[i].vx=-ball[i].vx
     if ball[i].bally>=190 and padx.padx-20<=ball[i].ballx<=padx.padx+20 :
        score+=1
        s+=1
        pyxel.play(0, [0,0])
     if ball[i].bally>=194.3 and (padx.padx-20>ball[i].ballx or padx.padx+20<ball[i].ballx) :
        pyxel.play(1, [1,1])
        error +=1
     if s % 11 == 0  :
        ball[i].speed=ball[i].speed*0.9
        ball.append(Ball())
        s+=1

def draw():
    global  score,error
    pyxel.cls(7)
    if error>=20 :
       pyxel.text(100,100,"game over!!",0)
    else :   
     for i in range(len(ball)) :
      pyxel.circ(ball[i].ballx, ball[i].bally, 10, 6)
     pyxel.rect(padx.padx-20, 195, 40, 5, 14)
     pyxel.text(10,10,"socre:"+str(score),0)
     pyxel.text(10,20,"error:"+str(error),0)
pyxel.run(update, draw)
# マウスのインスタンスを作りました