from tkinter import *
root = Tk()

def key(event):
    print("Pressed->" , repr(event.char))

def callBack(event):
    Frame.focus_set()
    print("Clicked at ->" , event.x , event.y)

frame = Frame(root , width = 300 , height=200)

frame.bind("<key>" , key)
frame.bind("<Button-1" , callBack)
frame.pack()
root.mainloop()
