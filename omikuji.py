import tkinter as tk
import random

result = ["大吉","小吉","吉","凶","大凶"]


def button_click():
    choice = random.choice(result)
    entry.config(state="normal")
    entry.delete(0,tk.END)
    entry.insert(0,choice)
    entry.config(state="readonly")


root = tk.Tk()
root.title("Omikuji")
root.geometry("300x300")

entry=tk.Entry(root,font=("Helvetica",20),justify="center",bd=10)
entry.pack(pady=30)

button = tk.Button(root,text="PUSH",font=("Helvetica"),command=button_click)
button.pack(pady=20)

root.mainloop()