import tkinter as tk
import math
import time

function = input("ievadi funkciju: y=")

root = tk.Tk()
root.title("yes")
root.geometry("500x500")
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack(anchor=tk.CENTER, expand=True)
canvas.create_line(250, 0, 250, 500, fill="black")
canvas.create_line(0, 250, 500, 250, fill="black")
for i in range(15):
    for x in range(-250, 251):
        try:
           y=eval(function, {"math": math, "x": x}, {"__builtins__": None})
           y=(-y)
           canvas.create_oval(x+249, y+249, x+252, y+252, fill="red", outline="red")
           print(y)
           root.update()
           time.sleep(0.001)
        except:
           pass
    time.sleep(0.1)
    for x in range(-250, 251):
        try:
           y=eval(function, {"math": math, "x": x}, {"__builtins__": None})
           y=(-y)
           canvas.create_oval(x+249, y+249, x+252, y+252, fill="blue", outline="blue")
           print(y)
           root.update()
           time.sleep(0.001)
        except:
           pass
    time.sleep(0.1)
root.mainloop()