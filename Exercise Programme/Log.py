from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()
tkWindow.geometry('1200x550')
tkWindow.title('Locals')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=4, column=5)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=4, column=6)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=5, column=4)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=6, column=6)

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)

tkWindow.mainloop()
Route for handling the login page logic
