
import keyboard
import pyperclip as pc
from tkinter import messagebox

Now = ""
Old = ""
t = ""
while True:
    if keyboard.read_key() == "esc":
        messagebox.showinfo("処理終了", "置換ツールを終了しました")
        break

    import pyperclip as pc
    Now = pc.paste()

    if Now != Old:
        if not '\\"' in Now:
            r = Now.replace('"', '\\"')
            pc.copy(r)
    Old = Now
