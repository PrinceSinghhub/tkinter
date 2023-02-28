from tkinter import *
root = Tk()
root.geometry('1080x720')
# 1 (1) font=("comicsansms",15,"bold")
# todo change gui name
root.title("codex coder")
label=Label(text='''\nThe U.S. National Academies of Sciences, Engineering,
                 \nand Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters)
                 \nof fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women''',bg="gray",fg="white",padx=100,pady=100,
            font="comicsansms 15 bold",borderwidth=10,relief=GROOVE)


label.pack()
root.mainloop()