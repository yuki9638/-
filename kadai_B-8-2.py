import pyxel

pyxel.init(200,200)

ballx = 100
bally = 0
vx = 0.866    # cos 60 degree
vy = 0.5  # sin 60 degree
speed =1.1

def update():
    global ballx, bally, vx, vy
    ballx += vx
    bally += vy
    if bally >= 200:
        ballx = 100
        bally = 0
        vx=vx*speed
        vy=vy*speed
    if ballx >=200 :
        vx=-0.866
    if ballx<=0 :
        vx=0.866

def draw():
    global ballx, bally, vx, vy
    pyxel.cls(7)
    pyxel.circ(ballx, bally, 10, 6)

pyxel.run(update, draw)
# 課題B-8-1に下に落ちるたびに傾きを変えるような処理を加えました。