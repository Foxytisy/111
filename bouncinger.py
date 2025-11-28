import tkinter as tk

mass_1 = float(input("Enter first cube mass"))
mass_2 = float(input("Enter big cube mass"))

bounceCounter = 0

#Canvas creation
root = tk.Tk()
root.title("yes")
root.geometry("800x500")
canvas = tk.Canvas(root, width=800, height=500, bg="black")
canvas.pack(anchor=tk.N, expand=True)

#bounce line creation
canvas.create_line(100, 50, 100, 450, fill="white")
canvas.create_line(100, 450, 700, 450, fill="white")

#Cube creation
cube1 = canvas.create_rectangle(150, 450, 200, 400, fill="yellow", outline="")
cube1vel = 0.0
cube2 = canvas.create_rectangle(400, 450, 500, 350, fill="blue", outline="")
cube2vel = -1.0

piText = canvas.create_text(20, 20, text="mau", fill="white")

def animate():
    global cube1vel, bounceCounter

    posCube1 = canvas.coords(cube1)
    posCube2 = canvas.coords(cube2)

    if posCube1[2] >= posCube2[0]:
        calcImpulss()
        bounceCounter+=1

    elif posCube1[0] <= 100:
        cube1vel=-cube1vel
        bounceCounter+=1
    print(posCube1,posCube2)

    canvas.move(cube1, cube1vel, 0)
    canvas.move(cube2, cube2vel, 0)

    canvas.itemconfig(piText, text=bounceCounter)

    root.after(10, animate)

def calcImpulss():
    global cube1vel, cube2vel, mass_1, mass_2
    cube1oldvel = cube1vel
    cube1vel = ((((mass_1-mass_2)/(mass_1+mass_2))*cube1vel)+(((2*mass_2)/(mass_1+mass_2))*cube2vel))
    cube2vel = ((((2*mass_1)/(mass_1+mass_2))*cube1oldvel)+(((mass_2-mass_1)/(mass_1+mass_2))*cube2vel))

animate()
root.mainloop()