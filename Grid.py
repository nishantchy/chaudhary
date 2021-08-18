from tkinter import *
root = Tk()
# creating a lael widget
mylabel1 = Label(root, text="hello World")
mylabel2 = Label(root, text="My name is Johny sins")

# shoving it into the screen
mylabel1.grid(row=0, column=0)
mylabel2.grid(row=1,column=1)


root.mainloop()

