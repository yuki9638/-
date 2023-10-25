import pyxel

pyxel.init(200,200)
pyxel.mouse(True)
angle = pyxel.rndi(30,150)
ballx= pyxel.rndi(0,199)
bally = 0
vx = pyxel.cos(angle)
vy = pyxel.sin(angle)
a= 0
speed =1.5
padx = 100

def update():
    global ballx, bally, vx, vy,padx,a
    ballx += vx*speed
    bally += vy*speed
    padx = pyxel.mouse_x
    if bally >= 196:
        ballx = 100
        bally = 0
        vx=vx*speed
        vy=vy*speed
    if ballx >=200 :
        vx=-0.866
    if ballx<=0 :
        vx=0.866
    if bally>=195 and padx-20<=ballx<=padx+20 :
        a+=1
def draw():
    global ballx, bally, vx, vy, padx,a
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)
    pyxel.rect(padx-20, 195, 40, 5, 14)
    pyxel.text(10,10,"socre:"+str(a),0)
pyxel.run(update, draw)