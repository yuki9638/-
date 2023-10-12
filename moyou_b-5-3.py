import pyxel

pyxel.init(200, 200)
pyxel.cls(0)
for a in range(10, 200, 20):
 for b in range(10,200,20) :
    if a<=-b+100 :
        pyxel.circ(a, b, 10, 6)
    elif a>=-b+300 :
      pyxel.circ(a,b,10,6)
    elif a<b-90 :
      pyxel.circ(a,b,10,6)
    elif a>=b+100 :
      pyxel.circ(a,b,10,6)
    elif b<=100 :
     pyxel.circ(a,b,10,13)
    elif a<=70 :
      pyxel.circ(a,b,10,6) 
    elif a>=130  :
         pyxel.circ(a,b,10,6)
    else :
      pyxel.circ(a, b, 10, 5)
pyxel.line(0,180,200,180,13)
pyxel.show()