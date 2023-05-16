from tkinter import *
root = Tk()

def rightClick(ev):
    print("Right Click")
def leftClick(ev):
    print("LeftClick")

def middleClick(ev):
    print("Middle Click")

frame = Frame(root , width =300 , height =200)

frame.bind("<Button-1>" , leftClick)
frame.bind("<Button-2>" ,middleClick )
frame.bind("<Button-3>" ,rightClick )
frame.pack()

root.mainloop()
