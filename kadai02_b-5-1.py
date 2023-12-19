import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(10, 200, 20):
 for b in range(10,200,20) :
    if a<=-b+100 :
        pyxel.circ(a, b, 10, 1)
    elif a>=-b+310 :
      pyxel.circ(a,b,10,14)
    elif a<=-b+200 :
     pyxel.circ(a,b,10,3)      
    else :
      pyxel.circ(a, b, 10, 6)
pyxel.show()
# 直線の上下で領域を指定し、その対応する領域に色を塗りました。
# その際、通常の座標軸とはy座標が逆転していることに注意しました