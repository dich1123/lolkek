from tkinter import *
import math, random

WIDTH = 100
HEIGHT = 100
in_move = True
colors = {'2': '#fdff9e', '4': '#fcff6d', '8': '#f9ff07', '16': '#ffd800',
          '32': '#ffc300', '64': '#ffa100', '128': '#ff9400',
          '256': '#ff6600', '512': '#ff4800', '1028': '#ff2600',
          '2048': '#b71b00', '4096': '#c24efc', '8192': '#5b79ff'}

places = [[15, 115], [130, 115], [245, 115], [360, 115],
          [15, 230], [130, 230], [245, 230], [360, 230],
          [15, 345], [130, 345], [245, 345], [360, 345],
          [15, 460], [130, 460], [245, 460], [360, 460]]

places_dict = {0: [15, 115], 1: [130, 115], 2: [245, 115], 3: [360, 115],
               4: [15, 230], 5: [130, 230], 6: [245, 230], 7: [360, 230],
               8: [15, 345], 9: [130, 345], 10: [245, 345], 11: [360, 345],
               12: [15, 460], 13: [130, 460], 14: [245, 460], 15: [360, 460]}


top = Tk()
top.geometry('475x575+100+100')
top.resizable(False, False)

c = Canvas(top, height=570, width=470, bg='#d1ceca')
c.create_text(10, -10, text='2048', font='Gagalin 90', anchor='nw')

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
# print(type(record))


def number_from_coords(coords):
    for i in places_dict.keys():
        if coords == places_dict[i]:
            return i


class Element:
    def __init__(self, x, y, value):  # x,y, value - int!!!!
        if str(value) in colors:
            color = colors[str(value)]
        else:
            color = '#5b79ff'
        self.rec = c.create_rectangle(x, y, x+HEIGHT, y+WIDTH,
                                      fill=color, outline=color)
        font = 'Gagalin '
        if len(str(value)) <= 3:
            font += '70'
        elif 5 > len(str(value)) > 3:
            font += '50'
        else:
            font += '40'
        self.value = c.create_text(x+HEIGHT/2, y+WIDTH/2,
                                   text=str(value), font=font, anchor='center')
        self.x = x
        self.y = y

    def destroy(self):
        c.delete(self.value)
        c.delete(self.rec)

    def move(self, x1, y1): # will slowly move to goal(x1, y1) WARNING! DO ONLY ONE STEP!
        global in_move
        in_move = False
        sign = lambda a: 1 if a > 0 else -1 if a < 0 else 0
        delta = int(HEIGHT/3)
        if math.fabs(x1 - self.x) > delta or math.fabs(y1 - self.y) > delta:
            self.x = self.x + (sign(x1-self.x)*(delta-3))
            self.y = self.y + (sign(y1-self.y)*(delta-3))
            c.coords(self.rec, self.x, self.y, self.x+HEIGHT, self.y+WIDTH)
            c.coords(self.value, self.x+HEIGHT/2, self.y+WIDTH/2)
            top.after(10, self.move, x1, y1)
        else:
            self.x = x1
            self.y = y1
            c.coords(self.value, self.x + HEIGHT / 2, self.y + WIDTH / 2)
            c.coords(self.rec, x1, y1, x1 + HEIGHT, y1 + WIDTH)
            in_move = True





class Pole:
    def __init__(self):
        pp = random.randint(0, 15)
        self.pole = {v: None for v in range(0, 16)}
        #  pp1 = random.choice(places)
        self.pole[pp] = Element(places_dict[pp][0], places_dict[pp][1],
                                random.choice([2, 4]))

    def add_element(self):
        chisla = [2, 4]
        if None in self.pole.values():
            while True:
                print('lol')
                pp = random.choice(places)
                ability = True
                for i in self.pole.values():
                    if i is not None:
                        if i.x == pp[0] and i.y == pp[1]:
                            ability = False
                            break
                if ability:
                    self.pole[number_from_coords(pp)] = (Element(pp[0], pp[1], random.choice(chisla)))
                    print('lolol')
                    break

    def one_line_move(self, a):
        pass


    def right_coords(self):
        pass








    def move(self, event):
        global in_move
        if event.keysym == 'Up' and in_move:
            for i in self.pole:
                if i is not None:
                    i.move(self.right_coords(i, 'Up')[0], self.right_coords(i, 'Up')[1])
            self.add_element()

        if event.keysym == 'Down' and in_move:
            for i in self.pole:
                i.move(360, 460)






cc = Pole()
top.bind_all('<KeyPress>', cc.move)
cc.add_element()
cc.add_element()
cc.add_element()

#cc = Element(places[0][0], places[0][1], 1024)





def main():
    top.after(15, main)


main()





top.mainloop()
