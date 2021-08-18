from tkinter import *
root = Tk()
def myclick():
	myLabel = Label(root, text="Look I clicked the button", fg="red", bg="pink")
	myLabel.pack()


myButton = Button(root, text="Click me!", command=myclick, padx=20, pady=20, fg="blue", bg="yellow")  
myButton.pack()



root.mainloop()

