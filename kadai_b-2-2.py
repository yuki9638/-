# 情基礎２の練習問題Bー２－２
import pyxel

pyxel.init(200, 200)
pyxel.cls(7)
for a in range(0,201,10) :
 pyxel.line(0, a, 200-a, 0, 0)
pyxel.show()
# 4行目で画面の範囲を指定し、５行目でクラスを指定、
# ６行目と７行目で直線を書くプログラムを実行し、８行目でその直線を画面に表示しています