from tkinter import *

#ability to write
def submit():
    write = entry.get()
#ability to delete
def delete():
    entry.delete(0, END)
#ability to backspace
def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()
window.geometry("500x500")

entry = Entry(window, font=("Arial", 50))
entry.pack(side=TOP) #puts the writing area on top

#submitButton = Button(window, text="submit", command=submit)
#submitButton.pack(side=RIGHT)

#deleteButton = Button(window, text="delete", command=delete)
#deleteButton.pack(side=RIGHT)

#backspaceButton = Button(window, text="backspace", command=backspace)
#backspaceButton.pack(side=RIGHT)

frame = Frame(window, bg="silver", bd=3)
frame.pack()
Button(frame, text="1", width=3).pack(side=LEFT)
Button(frame, text="2", width=3).pack(side=LEFT)
Button(frame, text="3", width=3).pack(side=LEFT)
Button(frame, text="4", width=3).pack(side=BOTTOM)
Button(frame, text="5", width=3).pack(side=BOTTOM)
Button(frame, text="6", width=3).pack(side=BOTTOM)
Button(frame, text="7", width=3).pack(side=BOTTOM)
Button(frame, text="8", width=3).pack(side=BOTTOM)
Button(frame, text="9", width=3).pack(side=BOTTOM)  

window.mainloop()
