import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(10, 200, 20):
    if ((a-10)/20) % 2 == 0:
        pyxel.circ(a, 10, 10, 0)
pyxel.show()