#15.29 H-tree fractal
from tkinter import *

class Htree:
    def __init__(self):
        window = Tk()
        window.title("H-tree Fractal")

        self.width = 200
        self.height = 200

        self.canvas = Canvas(window, width = self.width,
                             height = self.height)
        self.canvas.pack()

        frame1 = Frame(window)
        frame1.pack()

        Label(frame1, text = "Enter an order").pack(side = LEFT)
        self.order = StringVar()
        Entry(frame1, textvariable = self.order,
                      justify = RIGHT).pack(side = LEFT)
        Button(frame1, text = "Display",
               command = self.display).pack(side = LEFT)

        window.mainloop()

    def display(self):
        self.canvas.delete("line")
        center = [self.width / 2, self.height / 2]
        size = self.width / 4
        self.displayLine(int(self.order.get()), center, size)

    def displayLine(self, order, center, size):
        p1a = [center[0] - size, center[1]]
        p1b = [center[0] + size, center[1]]
        p2a = [p1a[0], p1a[1] - size]
        p2b = [p1a[0], p1a[1] + size]
        p3a = [p1b[0], p1b[1] - size]
        p3b = [p1b[0], p1b[1] + size]

        self.drawLine(p1a, p1b)
        self.drawLine(p2a, p2b)
        self.drawLine(p3a, p3b)
            
        if order > 0:
            self.displayLine(order - 1, p2a, size / 2)
            self.displayLine(order - 1, p2b, size / 2)
            self.displayLine(order - 1, p3a, size / 2)
            self.displayLine(order - 1, p3b, size / 2)

    def drawLine(self, p1, p2):
        self.canvas.create_line(p1[0], p1[1], p2[0], p2[1], tags = "line")

Htree()
            
            
        
    
