import pyxel

class Ball:
    speed = 1

    def __init__(self):
        self.restart()

    def move(self):
        self.ballx += self.vx
        self.bally += self.vy
        if self.ballx >= 200:
            self.vx = -self.vx
        if self.ballx <= 0:
            self.vx = -self.vx

    def restart(self):
        self.ballx = pyxel.rndi(0, 199)
        self.bally = 0
        self.ballr = 10
        self.angle = pyxel.rndi(30, 150)
        self.vx = pyxel.cos(self.angle)
        self.vy = pyxel.sin(self.angle)


class Padx:
    def __init__(self, app):  # Appクラスのインスタンスを受け取る
        self.app = app
        self.padx = pyxel.mouse_x
        self.pady = 195
        self.padw = 40
        self.padh = 5

    def catch(self, ball):
        for i in range(len(ball)):
            if 195 >= ball[i].bally >= 193 and self.padx - 20 <= ball[i].ballx <= self.padx + 20:
                self.app.score += 1  # Appクラスのscoreを更新
                self.app.s += 1       # Appクラスのsを更新
                return True
        return False
class Bullet:
    def __init__(self, x): # x座標は毎回変化できるように引数に。（色は変化させず、下端から発射するので一部を削除）
        self.x = x
        self.y = 200

    def move(self):
        self.y -= 5

    def draw(self):
        pyxel.circ(self.x, self.y, 2, 4)
class App:
    def __init__(self):
        pyxel.init(200, 200)
        pyxel.mouse(True)
        self.ball = [Ball()]
        self.pad = Padx(self)  # Appクラスのインスタンスを渡す
        self.score = 0
        pyxel.sound(0).set("e0e1c1", "p", "3", "s", 10)
        pyxel.sound(1).set("a2c3", "t", "7", "v", 50)
        self.error = 0
        self.s = 1
        self.bullets = []
    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            self.bullets.append(Bullet(pyxel.mouse_x))
        self.pad.padx = pyxel.mouse_x
        for i in range(len(self.ball)):
            self.ball[i].move()
            if self.ball[i].bally >= 197:
                self.ball[i].restart()
                self.ball[i].vx = self.ball[i].vx * self.ball[i].speed
                self.ball[i].vy = self.ball[i].vy * self.ball[i].speed
            if self.pad.catch(self.ball):
                pyxel.play(0, [0, 0])
            if not self.pad.catch(self.ball) and 195 >= self.ball[i].bally >= 193:
                pyxel.play(1, [1, 1])
                self.error += 1
            if self.s % 11 == 0:
                self.ball[i].speed = self.ball[i].speed * 0.9
                self.ball.append(Ball())
                self.s += 1
            for bullet in self.bullets:
                bullet.move()
                for s in range(len(self.bullets)): 
                 if self.ball[i].ballx-10<=self.bullets[s].x<=self.ball[i].ballx+10 and self.ball[i].bally-10<=self.bullets[sself.ball[i].restart()].y<=self.ball[i].bally+10 :
                    self.ball[i].restart()
    def draw(self):
        pyxel.cls(7)
        for bullet in self.bullets:
            bullet.draw()
        if self.error >= 20:
            pyxel.text(100, 100, "gameover", 0)
            return
        if self.score >= 100:
            pyxel.text(100, 100, "congraturation!", 0)
            return
        else:
            for i in range(len(self.ball)):
                pyxel.circ(self.ball[i].ballx, self.ball[i].bally, self.ball[i].ballr, 6)
            pyxel.rect(self.pad.padx, self.pad.pady, self.pad.padw, self.pad.padh, 14)
            pyxel.text(10, 20, "score:" + str(self.score), 0)
            pyxel.text(10,30 , "error:" + str(self.error), 0)
app = App()
pyxel.run(app.update, app.draw)
# バレットがボールに当たったらボールが元に戻るようにしました