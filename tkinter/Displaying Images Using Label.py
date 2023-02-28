from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.geometry('1080x720')
# photo=PhotoImage(file="Untitled.png")
# todo for jpg image
image=Image.open("10.jpg")
photo=ImageTk.PhotoImage(image)
pr=Label(image=photo)
pr.pack()
root.mainloop()