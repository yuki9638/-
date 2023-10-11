# ２重の繰り返しを使ったプログラム
import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(0,201,10) :
 for b in range(0,201,10) :
  pyxel.line(a, 0, b, 200, 0)
pyxel.show()
# 変数を二つ指定し、６行目と７行目で２重の繰り返しをしています