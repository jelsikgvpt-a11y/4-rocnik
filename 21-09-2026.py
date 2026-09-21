import tkinter as tk

win = tk.Tk()

canvas = tk.Canvas(win, width=1000, height=1000, bg = "green")
canvas.pack() 

def trojuholnik (a,x,y):
    if a > 10:
        canvas.create_line(x,y,x+a,y, fill ="yellow")
        canvas.create_line(x,y,x+a//2,y-(a**2-(a**2)/4)**0.5, fill ="yellow")
        canvas.create_line(x+a,y, x+a//2,y-(a**2-(a**2)/4)**0.5, fill ="yellow")
        trojuholnik(a//2,x,y)
        trojuholnik(a//2,x+a//2,y)
        
    
    
trojuholnik(900, 0, 900)








win.mainloop()