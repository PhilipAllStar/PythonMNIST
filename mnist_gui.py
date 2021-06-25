from os import close
from tkinter import *
import new_skript

def selectImg():
    print("select")

def startRec():
    print("start")

def exitPrg():
    window.destroy()
    exit()

window = Tk()
window.title('MNIST Number Recognition')
window.configure(background='white')

# label
Label(window, text='Handwritten Number Recognition', font='none 12 bold').grid(row=0, column=3)

selectButton = Button(window, text = 'Select your Image', command = selectImg)
selectButton.grid(row = 1, column = 0)

startButton = Button(window, text = 'Start Recognition', command = startRec)
startButton.grid(row = 1, column = 3)

exitButton = Button(window, text = 'Close Programm', command = exitPrg)
exitButton.grid(row = 10, column = 4)

#### run the mainloop
window.mainloop()