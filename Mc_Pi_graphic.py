from tkinter import *
from random import randint

inside = 0
piApprox = 0

def createCircle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
Canvas.createCircle = createCircle

class GUI():
    def __init__(self):
        main = Tk()
        main.geometry("1550x1100")
        main.attributes("-topmost", True)
        main.title("Monte Carlo Pi Approximation")
        
        self.canvas = Canvas(main, height=1100, width=1100)
        self.canvas.place(x=510, y=510, anchor=CENTER)
        self.canvas.createCircle(550, 550, 500, width=3)
        self.canvas.create_rectangle(50, 50, 1050, 1050, width=3)

        label = Label(main, text="Current Pi approximation:", font=("Arial", 25))
        label.place(x=1280, y=300, anchor=CENTER)
        self.piLabel = Label(main, text="0", font=("Arial", 50))
        self.piLabel.place(x=1280, y=375, anchor=CENTER)
        
        button = Button(main, text="Start", font=("Arial", 30), command= lambda: self.pointSimulation(10**6))
        button.place(x=1280, y=550, anchor=CENTER)

        main.mainloop()
    
    def pointSimulation(self, num):
        global inside, piApprox

        for i in range(num):
            xCoordinate = randint(50, 1050)
            yCoordinate = randint(50, 1050)
            x = xCoordinate - 550
            y = yCoordinate - 550

            if x**2+y**2 < 250000:
                inside += 1
                self.canvas.tag_lower(self.canvas.create_rectangle(xCoordinate, yCoordinate, xCoordinate, yCoordinate, outline="yellow"))
            else:
                self.canvas.tag_lower(self.canvas.create_rectangle(xCoordinate, yCoordinate, xCoordinate, yCoordinate, outline="red"))

            if i%100 == 99:
                piApprox = 4*inside/i
                self.piLabel.config(text=str(piApprox))
            self.piLabel.update()

if __name__ == "__main__":
    GUI()
