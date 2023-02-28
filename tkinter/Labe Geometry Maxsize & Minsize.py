from tkinter import *
root =Tk()
# todo set geometry widrh x height
root.geometry("600x600")
# todo minsize and max size widrh,height
root.maxsize(600,600)
root.minsize(600,600)
# todo make a label
pr=Label(text="codex coder")
pr.pack()
root.mainloop()