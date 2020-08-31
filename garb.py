import tkinter as tk

root = tk.Tk()

WIDTH = HEIGHT = 400

x1 = y1 = WIDTH / 2

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

c1 = canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10)
c2 = canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10)


def draw_rect():
    global c2
    canvas.delete(c2)
    c2 = canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10, fill="green")
    print(c2)


def del_rect():
    canvas.delete(c1)
    # canvas.create_rectangle(x1, y1, x1 + 10, y1 + 10, fill="white", opacity=0.5)


def move(event):
    global x1, y1
    if event.char == "a":
        del_rect()
        x1 -= 10
    elif event.char == "d":
        del_rect()
        x1 += 10
    elif event.char == "w":
        del_rect()
        y1 -= 10
    elif event.char == "s":
        del_rect()
        y1 += 10
    # draw_rect()
    draw_rect()


root.bind("<Key>", move)

root.mainloop()