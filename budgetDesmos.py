import tkinter as tk
import math
import time

func = input("ievadi funkciju: y=")
noValueCount = 0
noValueMaxCount = 500

#Satīra to funkcij (faktoriāļiem vajag izdomāt specgadījumu)
trans = {"^": "**", "sin": "math.sin", "cos": "math.cos", "tg": "math.tan", "sqrt": "math.sqrt", "log": "math.log"}
for i in trans:
    func = func.replace(i, trans[i])

#modulis
pos1 = 0
pos2 = 0
for ind, i in enumerate(func):
    if i == "|" and pos1 != 0:
       pos2 = ind+1
    elif i == "|":
       pos1 = ind+1
    if pos1 != 0 and pos2 != 0:
       func = func[:pos1-1] + "abs(" + func[pos1:pos2-1] + ")" + func[pos2:]
       pos1 = 0 
       pos2 = 0

#faktorials
pos1 = 0
pos2 = 0
for ind, i in enumerate(func):
    if i == "!" and pos1 != 0:
       pos2 = ind
    elif i in ["+", "-", "*", "/", "("] or ind == 0:
       pos1 = ind+1
    if ind != 0:
       pos1 =- 1
    if pos1 != 0 and pos2 != 0:
       func = func[:pos1-1] + "math.factorial(" + func[pos1-1:pos2] + ")" + func[pos2+1:]
       pos1 = 0 
       pos2 = 0

#Izveido to visu logu
root = tk.Tk()
root.title("yes")
root.geometry("500x500")
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack(anchor=tk.CENTER, expand=True)

#Koordinātu plaknes līnijas, tho vajadzētu pārtaisīt
canvas.create_line(250, 0, 250, 500, fill="black")
canvas.create_line(0, 250, 500, 250, fill="black")

#Pats tas zīmētājs
for i in range(15):
    for x in range(-250, 251):
        try:
           y=eval(func, {"math": math, "x": x}, {"__builtins__": None})
           y=(-y)
           canvas.create_oval(x+249, y+249, x+252, y+252, fill="red", outline="red")
           print(-y)
           root.update()
           noValueCount=0
           time.sleep(0.001)
        except:
            pass
            if noValueCount > noValueMaxCount:
             print("Error! 01")
             print(func)
             quit()
    time.sleep(0.1)
    for x in range(-250, 251):
        try:
           y=eval(func, {"math": math, "x": x}, {"__builtins__": None})
           y=(-y)
           canvas.create_oval(x+249, y+249, x+252, y+252, fill="blue", outline="blue")
           print(-y)
           root.update()
           time.sleep(0.001)
        except:
           pass
           if noValueCount > noValueMaxCount:
             print("Error! 01")
             print(func)
             quit()
    time.sleep(0.1)
#idk
root.mainloop()