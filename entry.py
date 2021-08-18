from tkinter import *
root = Tk()
e = Entry(root, width=10, bg="green", fg="white")
e.pack()

e.insert(0, "enter your name: ")
def myclick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello, fg="red", bg="pink")
	myLabel.pack()


myButton = Button(root, text="Enter your name", command=myclick, padx=20, pady=20, fg="blue", bg="yellow")  
myButton.pack()
e = Entry(root, width=30, bg="green", fg="white")
e.pack()
e.insert(0, "enter your name")
def myclick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello, fg="red", bg="pink")
	myLabel.pack()

myButton = Button(root, text="Enter your age", command=myclick, padx=20, pady=20, fg="blue", bg="yellow")
myButton.pack()
e = Entry(root, width=30, bg="green", fg="white")
e.pack()
e.insert(0, "enter your age")
def myclick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello, fg="red", bg="pink")
	myLabel.pack()

myButton = Button(root, text="Enter your phone number", command=myclick, padx=20, pady=20, fg="blue", bg="yellow")
myButton.pack()
e = Entry(root, width=30, bg="green", fg="white")
e.pack()
e.insert(0, "enter your number")
def myclick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello, fg="red", bg="pink")
	myLabel.pack()
myButton = Button(root, text="Postal code", command=myclick, padx=20, pady=20, fg="blue", bg="yellow")
myButton.pack()
e = Entry(root, width=10, bg="green", fg="white")
e.pack()

e.insert(0, "Postal code here ")
def myclick():
	hello = "Hello " + e.get()
	myLabel = Label(root, text=hello, fg="red", bg="pink")
	myLabel.pack()



root.mainloop()

