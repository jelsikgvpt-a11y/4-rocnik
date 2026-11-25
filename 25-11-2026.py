import tkinter as tk
win = tk.Tk()
win.title('Digi hodinky')
canvas = tk.Canvas(win, height = 500, width = 500, bg = 'white')
canvas.pack()

class Palicka:
    def __init__(self, canvas, x, y, dx, dy, color):
        self.id = canvas.create_rectangle(x,y,x+dx,y+dy, fill = color)
        self.canvas = canvas
    
    def on(self):
        self.canvas.itemconfig(self.id, state = 'normal')

    def off(self):
        self.canvas.itemconfig(self.id, state = 'hidden')

class Segment:
    def __init__(self,canvas,x,y,s,b,color):
        self.sticks = []
        self.sticks.append(Palicka(canvas, x+s,y,b,s,color))
        self.sticks.append(Palicka(canvas, x+s+b,y+s,s,b,color))
        self.sticks.append(Palicka(canvas, x+s,y+s+b,b,s,color))
        self.sticks.append(Palicka(canvas, x,y+s,s,b,color))
        self.sticks.append(Palicka(canvas, x+s+b,y+s+b+s,s,b,color))
        self.sticks.append(Palicka(canvas, x+s,y+s+s+b+b,b,s,color))
        self.sticks.append(Palicka(canvas, x,y+s+b+s,s,b,color))
        self.canvas = canvas

    def showall(self):
        for s in self.sticks:
            s.on()
    def hideall(self):
        for s in self.sticks:
            s.off()

    def show(self,number):
        if number == 0:
            self.showall()
            self.sticks[2].off()
        elif number == 1:
            self.hideall()
            self.sticks[1].on()
            self.sticks[4].on()
        elif number == 2:
            self.showall()
            self.sticks[4].off()
            self.sticks[3].off()
        elif number == 3:
            self.showall()
            self.sticks[3].off()
            self.sticks[6].off()
        elif number == 4:
            self.hideall()
            self.sticks[2].on()
            self.sticks[4].on()
            self.sticks[3].on()
            self.sticks[1].on()
        elif number == 5:
            self.showall()
            self.sticks[1].off()
            self.sticks[6].off()
        elif number == 6:
            self.showall()
            self.sticks[1].off()
        elif number == 7:
            self.hideall()
            self.sticks[0].on()
            self.sticks[1].on()
            self.sticks[4].on()
        elif number == 8:
            self.showall()
        elif number == 9:
            self.showall()
            self.sticks[6].off()

segment  = Segment(canvas,100,100,20,80,'green')
segment.show(6)
win.mainloop()