from tkinter import *
import random

WIDTH = 100
HEIGHT = 100
in_move = True
colors = {'2': '#fdff9e', '4': '#fcff6d', '8': '#f9ff07', '16': '#ffd800',
          '32': '#ffc300', '64': '#ffa100', '128': '#ff9400',
          '256': '#ff6600', '512': '#ff4800', '1024': '#ff2600',
          '2048': '#b71b00', '4096': '#c24efc', '8192': '#5b79ff'}

places = [[15, 115], [130, 115], [245, 115], [360, 115],
          [15, 230], [130, 230], [245, 230], [360, 230],
          [15, 345], [130, 345], [245, 345], [360, 345],
          [15, 460], [130, 460], [245, 460], [360, 460]]

places_like_pole = [[[15, 115], [130, 115], [245, 115], [360, 115]],
                    [[15, 230], [130, 230], [245, 230], [360, 230]],
                    [[15, 345], [130, 345], [245, 345], [360, 345]],
                    [[15, 460], [130, 460], [245, 460], [360, 460]]]

places_dict = {0: [15, 115], 1: [130, 115], 2: [245, 115], 3: [360, 115],
               4: [15, 230], 5: [130, 230], 6: [245, 230], 7: [360, 230],
               8: [15, 345], 9: [130, 345], 10: [245, 345], 11: [360, 345],
               12: [15, 460], 13: [130, 460], 14: [245, 460], 15: [360, 460]}


top = Tk()
top.geometry('475x575+100+100')
top.resizable(False, False)

c = Canvas(top, height=570, width=470, bg='#d1ceca')
c.create_text(10, -10, text='2048', font='Gagalin 70', anchor='nw')

c.create_rectangle(0, 100, 545, 115, fill='#a8a39c', outline='#a8a39c')
c.create_rectangle(0, 215, 545, 230, fill='#a8a39c', outline='#a8a39c')
c.create_rectangle(0, 330, 545, 345, fill='#a8a39c', outline='#a8a39c')
c.create_rectangle(0, 445, 545, 460, fill='#a8a39c', outline='#a8a39c')
c.create_rectangle(0, 560, 545, 575, fill='#a8a39c', outline='#a8a39c')

c.create_rectangle(0, 100, 15, 615, fill='#a8a39c', outline='#a8a39c')
c.create_rectangle(115, 100, 130, 615, fill='#a8a39c', outline='#a8a39c')
c.create_rectangle(230, 100, 245, 615, fill='#a8a39c', outline='#a8a39c')
c.create_rectangle(345, 100, 360, 615, fill='#a8a39c', outline='#a8a39c')
c.create_rectangle(460, 100, 475, 615, fill='#a8a39c', outline='#a8a39c')
c.pack()

score = c.create_text(200, 10, text='score:', font='Gagalin 30', anchor='nw')
record = c.create_text(200, 50, text='record:', font='Gagalin 30', anchor='nw')


blocks = []  #


def create_field_element(value, pos_x, pos_y):
    if value == '_':
        return

    block = []

    if str(value) in colors:
        color = colors[str(value)]
    else:
        color = '#5b79ff'
    bg = c.create_rectangle(pos_x, pos_y, pos_x + HEIGHT, pos_y + WIDTH,
                            fill=color, outline=color)
    block.append(bg)

    font = 'Gagalin '
    if len(str(value)) < 3:
        font += '70'
    elif len(str(value)) < 4:
        font += '45'
    elif len(str(value)) < 5:
        font += '35'
    else:
        font += '20'
    num = c.create_text(pos_x + HEIGHT / 2, pos_y + WIDTH / 2,
                        text=str(value), font=font, anchor='center')
    block.append(num)

    return block


def show(pole):
    for i in range(len(pole)):
        for j in range(len(pole)):
            x, y = places_like_pole[i][j]

            block = create_field_element(pole[i][j], x, y)
            if block is not None:
                blocks.append(block)


def clear():
    for block in blocks:
        c.delete(block[0])
        c.delete(block[1])


# START OF BACK CODE


# END OF BACK CODE


def move(event):
    global pole

    if event.char == "a":
        pole = igra(pole, 'a')
    elif event.char == "d":
        pole = igra(pole, 'd')
    elif event.char == "w":
        pole = igra(pole, 'w')
    elif event.char == "s":
        pole = igra(pole, 's')
    else:
        return
    pole = rand_hod(pole)
    clear()
    show(pole)

pole = rand_hod(pole)
show(pole)

top.bind("<Key>", move)

top.mainloop()