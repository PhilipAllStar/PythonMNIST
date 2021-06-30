from os import close
from tkinter import filedialog as fd
from tkinter import *
from warnings import catch_warnings

from tensorflow.python.keras.backend import cast_variables_to_tensor
from tensorflow.python.summary.summary import image
import new_skript
from PIL import ImageTk, Image
import cv2

def selectImg():
    file = fd.askopenfilename(filetypes=[('all files','*')])
    filetoprocess = Image.open(file)
    newImg = ImageTk.PhotoImage(filetoprocess)
    
    l.configure(image=newImg)
    l.image = newImg

    

def startRec():
    prediction = new_skript.predict2()

def exitPrg():
    window.destroy()
    exit()

window = Tk()
window.title('MNIST Number Recognition')
window.geometry("700x400")
window.configure(background='grey')

Label(window, text='Handwritten Number Recognition', font='none 12 bold').pack() #.grid(row=0, column=3)

selectButton = Button(window, text = 'Select your Image', command = selectImg) #.grid(row = 1, column = 0)
selectButton.pack()

startButton = Button(window, text = 'Start Recognition', command = startRec)#.grid(row = 1, column = 3)
startButton.pack()

img = ImageTk.PhotoImage(Image.open("img_1021.jpg"))  
l=Label(image=img)
l.pack()

predictionLabel = Label(window, text= 'Prediction: ' )#.grid(row=4, column=3)
predictionLabel.pack()

exitButton = Button(window, text = 'Close Programm', command = exitPrg)#.grid(row = 10, column = 4)
exitButton. pack()
#### run the mainloop
window.mainloop()
