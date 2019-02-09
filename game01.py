from tkinter import *
import random

button = []

def pushed(num, self):
    for i in range(3):
        self[i]["bg"] = "#eee"
        button[i]["state"] = "disabled"
    self[num]["bg"] = "#e25"

    kenji = random.randint(0,2)

    if num == kenji:
        label2["text"] = "あいこ"
    if num == 0:
        label4["text"] = "ぐー"
        if kenji == 1:
            label2["text"] = "勝ち"
            label2["foreground"] = "#f00"
        elif kenji == 2:
            label2["text"] = "負け"
            label2["foreground"] = "#00f"
    elif num == 1:
        label4["text"] = "ちょき"
        if kenji == 2:
            label2["text"] = "勝ち"
            label2["foreground"] = "#f00"
        elif kenji == 0:
            label2["text"] = "負け"
            label2["foreground"] = "#00f"
    else:
        label4["text"] = "ぱー"
        if kenji == 0:
            label2["text"] = "勝ち"
            label2["foreground"] = "#f00"
        elif kenji == 1:
            label2["text"] = "負け"
            label2["foreground"] = "#00f"

    if kenji == 0:
        label6["text"] = "ぐー"
    elif kenji == 1:
        label6["text"] = "ちょき"
    else:
        label6["text"] = "ぱー"

def reset(self):
    for i in range(3):
        self[i]["bg"] = "#eee"
        self[i]["state"] = "normal"
    label1["text"] = "じゃんけん"
    label2["text"] = ""
    label4["text"] = ""
    label6["text"] = ""
    label2["foreground"] = "#000"

root = Tk()
root.geometry("500x300+10+20")
root.title("game01")

f1 = Frame(root)
label1 = Label(f1, text="じゃんけん", font=("arial", 20, "bold"))
label2 = Label(f1, text="", font=("arial", 26, "bold"))
label1.pack()
label2.pack()
f1.place(relx=0.35, rely=0.05)

f2 = Frame(root)
label3 = Label(f2, text="プレイヤー1")
label4 = Label(f2, text="", font=(30),width=10, height=5, bg="#ddd")
label5 = Label(f2, text="ジャン健二")
label6 = Label(f2, text="", font=(30),width=10, height=5, bg="#ddd")
label3.grid(row=0, column=0, padx=10)
label4.grid(row=1, column=0, padx=10)
label5.grid(row=0, column=1, padx=130)
label6.grid(row=1, column=1, padx=130)
f2.place(relx=0.1, rely=0.3)

f3 = Frame(root)
button.append(Button(f3, text="ぐー", width=5, height=2, command=lambda:pushed(0,button)))
button.append(Button(f3, text="ちょき", width=5, height=2, command=lambda:pushed(1,button)))
button.append(Button(f3, text="ぱー", width=5, height=2, command=lambda:pushed(2,button)))
button.append(Button(f3, text="次のゲームへ", width=8, height=3, command=lambda:reset(button)))
button[0].grid(row=0, column=0, pady=0)
button[1].grid(row=1, column=0, pady=0)
button[2].grid(row=2, column=0, pady=0)
button[3].grid(row=3, column=0, pady=7)
f3.place(relx=0.45, rely=0.33)

root.mainloop()
