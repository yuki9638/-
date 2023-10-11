import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(10, 200, 20):
 for b in range(10,200,20) :
    if ((a-10)/20) % 2 == 0:
     if ((b-10)/20)%2 == 0 :
        pyxel.circ(a, b, 10, 6)
     else :
       pyxel.circ(a,b,10,14)      
    elif ((b-10)/20)%2 == 0 : 
     if ((a-10)/20)%2 != 0 :  
        pyxel.circ(a, b, 10, 14)
    else :
      pyxel.circ(a, b, 10, 6)
pyxel.show()
# 縦の行と横の行の円を個数の単位に還元し、その数字の奇遇で場合分けをしました