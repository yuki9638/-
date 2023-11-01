import pyxel

pyxel.init(200,200)
pyxel.mouse(True)
angle1 = pyxel.rndi(30,150)
angle2 = pyxel.rndi(30,150)
angle3 = pyxel.rndi(30,150)
ballx= [pyxel.rndi(0,200),pyxel.rndi(0,200),pyxel.rndi(0,200)]
bally = [0,0,0]
vx = [pyxel.cos(angle1),pyxel.cos(angle2),pyxel.cos(angle3)]
vy = [pyxel.sin(angle1),pyxel.sin(angle2),pyxel.sin(angle3)]
a= 0
speed =1.5
padx = 100
pyxel.sound(0).set("e0e1c1","p","3","s",10)

pyxel.sound(1).set("a2c3","t","7","v",50)
def update():
    global ballx, bally, vx, vy,padx,a
    padx=pyxel.mouse_x
    for i in range(0,len(ballx)) :
     ballx[i] += vx[i]*speed
     bally[i] += vy[i]*speed
     if bally[i] >= 196:
        ballx[i] = pyxel.rndi(0,199)
        bally[i] = 0
        vx[i]=vx[i]*speed
        vy[i]=vy[i]
     if ballx[i]>200 :
         vx[i]=-0.866
     if ballx[i]<=0 :
        vx[i]=0.866
     if bally[i]>=195 and padx-20<=ballx[i]<=padx+20 :
        a+=1
        pyxel.play(0, [0,0])
     if bally[i]>=195 and (padx-20>ballx[i] or padx+20<ballx[i]) :
        pyxel.play(1, [1,1])
def draw():
    global ballx, bally, vx, vy, padx,a
    pyxel.cls(7)
    for i in range(0,len(ballx)) :
     pyxel.circ(ballx[i], bally[i], 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)
    pyxel.text(10,10,"socre:"+str(a),0)
pyxel.run(update, draw)
# ボールを三個にしました。繰り返しでfor文を最初に使わなくてはいけないということと、インデントをそろえないといけないということに注意して書きました。