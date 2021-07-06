from os import close
from tkinter import messagebox
from tkinter import filedialog as fd
from tkinter import *
from warnings import catch_warnings

from tensorflow.python.keras.backend import cast_variables_to_tensor
from tensorflow.python.summary.summary import image
import new_skript
from PIL import ImageTk, Image
import numpy as np
import cv2 as cv

file2process = 0
prediction: any

def selectImg():
    global file2process
    file = fd.askopenfilename(filetypes=[('png Pictures', '.png'), ('jpg Pictures', '.jpg'), ('jpeg Pictures', '.jpeg')])    #get filepath
    print(file)
    if file != '':
        try:
            file2process = Image.open(file)
        except:
            messagebox.showerror('Wrong filetype', 'Please select a filetype of .png , .jpg')

        newImg = ImageTk.PhotoImage(file2process)
        l.configure(image=newImg)
        l.image = newImg
    else:
        messagebox.showerror('No file selected', 'Please select a file.')

def startRec():
    if file2process != 0:
        #get predictions
        predictions = new_skript.predict(file2process)

        # show results
        showPrediction(predictions)
    else: 
        messagebox.showerror('No file/image', 'Please selcet a file before you start the recognition process.')

def showPrediction(array):
    print(array)
    uSure = 0 
    for x in array:
        if (x >= 0.9):
            predictionLabel.configure(text= "Prediction: " + str(np.argmax(array)))
            uSure = 1
            break
    if (uSure == 0):
        predictionLabel.configure(text="Probably not an number.")

def exitPrg():
    result = messagebox.askquestion("Exit Program", "Are you sure you want to exit?", icon='warning')
    if result == 'yes':
        window.destroy()
        exit()

window = Tk()
window.title('MNIST Number Recognition')
window.geometry("700x400")
window.configure(background='grey')

Label(window, text='Handwritten Number Recognition', font='none 12 bold').pack()

selectButton = Button(window, text = 'Select your Image', command = selectImg)
selectButton.pack()

startButton = Button(window, text = 'Start Recognition', command = startRec)
startButton.pack()

l=Label()
l.pack()

predictionLabel = Label(window, text= 'Prediction: ' )
predictionLabel.pack()

exitButton = Button(window, text = 'Close Programm', command = exitPrg)
exitButton.pack()

#### run the mainloop
window.mainloop()
