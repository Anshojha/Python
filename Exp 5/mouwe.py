

from tkinter import*

root = Tk()
def rightclick(ev):
    print("Right Click!!")

def leftclick(ev):
    print("Left click")

def middleclick(ev):
    print("Middle Click")


frame = Frame(root,width=300,height=200)
frame = Frame(root,width=300,height=200)
frame.bind("<Button-1>",leftclick)
frame.bind("<Button-2>",middleclick)
frame.bind("<Button-3>",rightclick)
frame.pack()
root.mainloop()



