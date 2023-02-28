from tkinter import *
root=Tk()
root.geometry("1080x720")
label=Label(text="codex coder",bg="gray",fg="black",relief=GROOVE,font="comicsansms 100 bold")
# todo anchor
# todo side=BOTTOM,LEFT,RIGHT,TOP by default anchor is top
# label.pack(side=LEFT,anchor="se")
# is we want to out tsxr in middele the use
# todo filll x or y
# todo label.pack(side=BOTTOM,fill='x')
# if we fill y then
# label.pack(side=LEFT,fill='y')
# todo use padx and pady
label.pack(side=LEFT,fill='y',padx='60',pady='40')
root.mainloop()