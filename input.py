import pyxel

# Pyxelの初期化
pyxel.init(width=160, height=120)

# 入力された文字列を格納する変数
user_input = ""

# ゲームの更新ロジック
def update():
    global user_input

    # 何かしらの更新処理

    # キーが押されたら文字列を構築
    for key in pyxel.KEY_LIST:
        if pyxel.btnp(key):
            if key == pyxel.KEY_ENTER:
                # Enterキーが押されたら入力を確定
                print("User input:", user_input)
                user_input = ""
            elif key == pyxel.KEY_BACKSPACE:
                # Backspaceキーが押されたら最後の文字を削除
                user_input = user_input[:-1]
            else:
                # 他のキーが押されたら文字列に追加
                user_input += chr(key)

# ゲームの描画ロジック
def draw():
    pyxel.cls(0)
    
    # 入力された文字列を描画
    pyxel.text(10, 10, "User input: " + user_input, 7)

# Pyxelの実行
pyxel.run(update, draw)
