# ボールを操作して、水色のボールにあてることによって得点を稼ぐゲームを作りました。ミスが２０回以上でゲームおーば
# 成功が１００回以上で成功です。
import pyxel

pyxel.init(200,200)
pyxel.mouse(True)
angle = [pyxel.rndi(30,150)]
ballx= [pyxel.rndi(0,199)]
bally = [pyxel.rndi(0,150)]
vx = [pyxel.cos(angle[0])]
vy = [pyxel.sin(angle[0])]
score= 0
speed =1.1
padx=pyxel.mouse_x
pady=pyxel.mouse_y
pyxel.sound(0).set("e0e1c1","p","3","s",10)

pyxel.sound(1).set("a2c3","t","7","v",50)
error=0
s=1
def update():
    global ballx, bally, vx, vy,padx,pady,score,angle,error,s,speed
    for i in range (len(ballx)) :
     ballx[i] += vx[i]
     bally[i] += vy[i]
     padx = pyxel.mouse_x
     pady =pyxel.mouse_y
     if bally[i] >= 196:
        ballx[i] = pyxel.rndi(0,199)
        bally[i] = 0
        vx[i]=vx[i]*speed
        vy[i]=vy[i]*speed
     if ballx[i] >=200 :
        vx[i]=-vx[i]
     if ballx[i]<=0 :
        vx[i]=-vx[i]
     if pady-10<bally[i]<pady+10 and padx-10<=ballx[i]<=padx+10 :
        score+=1
        s+=1
        pyxel.play(0, [0,0])
        bally[i]=pyxel.rndi(0,150)
        ballx[i]=pyxel.rndi(0,199)
        vx[i]=vx[i]*speed
        vy[i]=vy[i]*speed
     if bally[i]>=194.3 :
        pyxel.play(1, [1,1])
        error +=1
     if s % 11 == 0  :
        speed=speed*0.95
        ballx.append(pyxel.rndi(0, 199))
        bally.append(0)
        angle.append(pyxel.rndi(30, 150))
        vx.append(pyxel.cos(angle[-1]))
        vy.append(pyxel.sin(angle[-1]))
        s+=1

def draw():
    global ballx, bally, vx, vy, padx,pady,score,error
    pyxel.cls(7)
    if error>=20 :
       pyxel.text(90,190,"game over!!",0)
    elif score>=100 :
       pyxel.text(90,90,"congratulation!!",0)
    else :   
     for i in range(len(ballx)) :
      pyxel.circ(ballx[i], bally[i], 10, 6)
     pyxel.circ(padx, pady,10,  14)
     pyxel.text(10,10,"socre:"+str(score),0)
     pyxel.text(10,20,"error:"+str(error),0)
pyxel.run(update, draw)