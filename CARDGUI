import tkinter
from tkinter import *
from PIL import Image,ImageTk

root = Tk()

# Create a photoimage object of the image in the path
image1 = Image.open('cards.png')
cards = {}
for i in range(4):
    for l in range(13):
        a = l*79
        b = i*123
        c = (l+1)*79
        d = (i+1)*123
        cropped = image1.crop((a,b,c,d)) #a = top left b = bottom left c = top right d = bottom right
        test = ImageTk.PhotoImage(cropped)
        label = tkinter.Label(image=test)
        label.image = test
        if i == 0:
            suit = "Clubs"
            rank = str(l)
            card = rank + " " + suit
            cards[card] = [label]
        if i == 1:
            suit = "Diamonds"
            rank = str(l)
            card = rank + " " + suit
            cards[card] = [label]
        if i == 2:
            suit = "Hearts"
            rank = str(l)
            card = rank + " " + suit
            cards[card] = [label]
        if i == 3:
            suit = "Spades"
            rank = str(l)
            card = rank + " " + suit
            cards[card] = [label]

cards["10 Clubs"][0].place(x=10, y=100)



# Position image

root.mainloop()