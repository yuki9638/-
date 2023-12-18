import pyxel

class App:
    def __init__(self):
        pyxel.init(200,200)
        
        pyxel.run(self.update, self.draw)  

    def update(self):
        self.user_input=input()
        
    def draw(self):
        pyxel.cls(7) 
        pyxel.text(150,20,"Type this strings",1)
        if self.user_input=="a":
            pyxel.text(100, 100, "congraturation!", 0)
App()
        