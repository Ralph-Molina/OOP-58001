from tkinter import *
from tkinter import ttk
window = Tk()

def Putherename():
    txtfld['text'] = 'Testing'

window.geometry("500x250+10+20")
window.title("Midterm in OOP")

label = Label(window, text = "Enter your fullname:", fg = "Red")
label.place(x=65, y=70)

button = Button(window, text = "Click to display your Fullname", fg = "Red", command=Putherename)
button.place (x=70, y=150)

txtfld = Entry(window, textvariable = 'Testing', bd = 5)
txtfld.place(x=270, y=70)

txtfld = Entry(window, text = 'testingname', bd = 5)
txtfld.place(x=270, y=150)

window.mainloop()