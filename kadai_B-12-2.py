import pyxel

pyxel.init(200,200)
pyxel.mouse(True)
class Ball :
  speed=1
  def __init__(self):
   self.restart()
  def move(self):   
     self.ballx += self.vx
     self.bally += self.vy
     if self.ballx >=200 :
        self.vx=-self.vx
     if self.ballx<=0 :
        self.vx=-self.vx
  def restart(self) : 
        self.ballx = pyxel.rndi(0,199)
        self.bally = 0
        self.ballr=10
        self.angle = pyxel.rndi(30,150)
        self.vx = pyxel.cos(self.angle)
        self.vy = pyxel.sin(self.angle)
ball =[Ball()]
class Padx :
  def __init__(self):
   self.padx = pyxel.mouse_x -20
   self.pady=195
   self.padw=40
   self.padh=5
pad=Padx()
score = 0
pyxel.sound(0).set("e0e1c1","p","3","s",10)

pyxel.sound(1).set("a2c3","t","7","v",50)
error=0
s=1
def update():
    global score,angle,error,s,speed
    pad.padx = pyxel.mouse_x
    for i in range (len(ball)) :
     ball[i].move()
     if ball[i].bally >= 196: 
      ball[i].restart()
      ball[i].vx=ball[i].vx*ball[i].speed
      ball[i].vy=ball[i].vy*ball[i].speed      
     if ball[i].bally>=190 and pad.padx-20<=ball[i].ballx<=pad.padx+20 :
        score+=1
        s+=1
        pyxel.play(0, [0,0])
     if ball[i].bally>=194.3 and (pad.padx-20>ball[i].ballx or pad.padx+20<ball[i].ballx) :
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
    elif score>=100 :
       pyxel.text(100,100,"conguraturation",0)
    else :   
     for i in range(len(ball)) :
      pyxel.circ(ball[i].ballx, ball[i].bally, ball[i].ballr, 6)
     pyxel.rect(pad.padx, pad.pady, pad.padw, pad.padh, 14)
     pyxel.text(10,10,"socre:"+str(score),0)
     pyxel.text(10,20,"error:"+str(error),0)
pyxel.run(update, draw)
# リスタートメソッドを新たにボールクラス内に作りました