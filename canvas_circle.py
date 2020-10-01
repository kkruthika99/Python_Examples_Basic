From tkinter import *
def DrawCircle():
canvas.create_oval(10,10,200,200)
root=Tk()
canvas=Canvas(root)
button=Button(root,text="DRAW CIRCLE",command=lambda :DrawCircle())
canvas.pack()
button.pack()
root.mainloop()
