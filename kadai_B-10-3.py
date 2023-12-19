import pyxel

pyxel.init(200,200)
pyxel.mouse(True)
angle = [pyxel.rndi(30,150)]
ballx= [pyxel.rndi(0,199)]
bally = [0]
vx = [pyxel.cos(angle[0])]
vy = [pyxel.sin(angle[0])]
score= 0
speed =1.3
padx = 100
pyxel.sound(0).set("e0e1c1","p","3","s",10)

pyxel.sound(1).set("a2c3","t","7","v",50)
error=0
s=1
def update():
    global ballx, bally, vx, vy,padx,score,angle,error,s,speed
    for i in range (len(ballx)) :
     ballx[i] += vx[i]*speed
     bally[i] += vy[i]*speed
     padx = pyxel.mouse_x
     if bally[i] >= 196:
        ballx[i] = pyxel.rndi(0,199)
        bally[i] = 0
        vx[i]=vx[i]*speed
        vy[i]=vy[i]*speed
     if ballx[i] >=200 :
        vx[i]=-vx[i]
     if ballx[i]<=0 :
        vx[i]=-vx[i]
     if bally[i]>=194.3 and padx-20<=ballx[i]<=padx+20 :
        score+=1
        s+=1
        pyxel.play(0, [0,0])
     if bally[i]>=194.3 and (padx-20>ballx[i] or padx+20<ballx[i]) :
        pyxel.play(1, [1,1])
        error +=1
     if s % 11 == 0  :
        speed=speed*0.9
        ballx.append(pyxel.rndi(0, 199))
        bally.append(0)
        angle.append(pyxel.rndi(30, 150))
        vx.append(pyxel.cos(angle[-1]))
        vy.append(pyxel.sin(angle[-1]))
        s+=1

def draw():
    global ballx, bally, vx, vy, padx,score,error
    pyxel.cls(7)
    if error>=20 :
       pyxel.text(100,100,"game over!!",0)
    else :   
     for i in range(len(ballx)) :
      pyxel.circ(ballx[i], bally[i], 10, 6)
     pyxel.rect(padx-20, 195, 40, 5, 14)
     pyxel.text(10,10,"socre:"+str(score),0)
     pyxel.text(10,20,"error:"+str(error),0)
pyxel.run(update, draw)
# 得点が十増えるごとにボールの数が一つ増えるという処理をそのまま書くと無限にボールが増え続けてしまう
# ので別の変数を定義して管理をするようにしました。