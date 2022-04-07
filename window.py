from tkinter import *
import numsnsym

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

entry = Entry(window, font = ("Arial", 50))
entry.pack(side=LEFT)

submitButton = Button(window, text="submit", command=submit)
submitButton.pack(side=RIGHT)

deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack(side=RIGHT)

backspaceButton = Button(window, text="backspace", command=backspace)
backspaceButton.pack(side=RIGHT)

OneButton = Button(window, text="1", command=lambda: numsnsym.one(1))
OneButton.pack(side=TOP)
#TwoButton = Button(window, text="2", command=)
#ThreeButton = Button(window, text="3", command=)
#FourButton = Button(window, text="4", command=)
#FiveButton = Button(window, text="5", command=)
#SixButton = Button(window, text="6", command=)
#SevenButton = Button(window, text="7", command=)
#EightButton = Button(window, text="8", command=)
#NineButton = Button(window, text="9", command=)




window.mainloop()
