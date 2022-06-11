from tkinter import *
from tkinter import ttk
import tkinter as tk
# ------------------------------------------------
# window = Tk()
# window.geometry('500x500+150+150')
# window.title('Hello Tkinter')
# window.configure(bg='white')
# window.mainloop()

# ------------------------------------------------
# window = Tk()
# window.geometry('500x500+500+150')
# window.title('Hello Tkinter')
# b = Button(text='Hello', fg='red').pack(pady=10)
# b1 = Button(text='Hello', fg='red', state=DISABLED).pack(pady=10)
# l = Label(text='Hello', fg='red', bg='black').pack()
# window.mainloop()

# ------------------------------------------------
# place depends on x and y coordinates
# grid depends on columns and rows
# window = Tk()
# window.geometry('500x500+500+150')
# window.title('Hello Tkinter')
# b = Button(text='Hello', fg='red').place(x=200, y=250)
# l = Label(text='Hello', fg='red', bg='black').place(x=200, y=250)
# b2 = Button(text='Hello', fg='red').place(x=200, y=250)
# l2 = Label(text='Hello', fg='red', bg='black').place(x=400, y=250)
# window.mainloop()

# window = Tk()
# window.geometry('500x500+500+150')
# window.title('Hello Tkinter')
# b = Button(text='Hello', fg='red').grid(column=0, row=0)
# l = Label(text='Hello', fg='red', bg='black').grid(column=1, row=1)
# window.mainloop()

# ------------------------------------------------
# FLAT
# RAISED
# SUNKEN
# GROOVE
# RIDGE

# window = Tk()
# window.geometry('500x500+500+150')
# window.title('Hello Tkinter')
# b1 = Button(text='FLAT  ', relief=FLAT).pack()
# b2 = Button(text='RAISED', relief=RAISED).pack()
# b3 = Button(text='SUNKEN', relief=SUNKEN).pack()
# b4 = Button(text='GROOVE', relief=GROOVE).pack()
# b5 = Button(text='RIDGE ', relief=RIDGE).pack()
# window.mainloop()
# ------------------------------------------------
# "error"
# "gray75"
# "gray50"
# "gray25"
# "gray12"
# "hourglass"
# "info"
# "questhead"
# "question"
# "warning"

# window = Tk()
# window.geometry('500x500+500+150')
# window.title('Hello Tkinter')
# b1 = Button(text='FLAT  ', bg='white', bitmap="error").pack()
# b2 = Button(text='RAISED', bg='white', bitmap="gray75").pack()
# b3 = Button(text='SUNKEN', bg='white', bitmap="gray50").pack()
# b4 = Button(text='GROOVE', bg='white', bitmap="gray25").pack()
# b5 = Button(text='RIDGE ', bg='white', bitmap="gray12").pack()
# b6 = Button(text='FLAT  ', bg='white', bitmap="hourglass").pack()
# b7 = Button(text='RAISED', bg='white', bitmap="info").pack()
# b8 = Button(text='SUNKEN', bg='white', bitmap="questhead").pack()
# b9 = Button(text='GROOVE', bg='white', bitmap="question").pack()
# b10 = Button(text='RIDGE ', bg='white', bitmap="warning").pack()
# window.mainloop()
# ------------------------------------------------

# "arrow"    "circle"  "clock"
# "cross"    "dotbox"  "exchange"
# "fleur"    "heart"   "man"
# "mouse"    "pirate"  "plus"
# "shuttle"  "sizing"  "spider"
# "spraycan" "star"    "target"
# "tcross"   "trek"    "watch"

# window = Tk()
# window.geometry('500x500+500+150')
# window.title('Hello Tkinter')
# b1 = Button(text='Hello', bg='white', cursor="arrow").pack()
# b2 = Button(text='Hello', bg='white', cursor="circle").pack()
# b3 = Button(text='Hello', bg='white', cursor="clock").pack()
# b4 = Button(text='Hello', bg='white', cursor="cross").pack()
# b5 = Button(text='Hello', bg='white', cursor="dotbox").pack()
# b6 = Button(text='Hello', bg='white', cursor="man").pack()
# b7 = Button(text='Hello', bg='white', cursor="heart").pack()
# b8 = Button(text='Hello', bg='white', cursor="fleur").pack()
# b9 = Button(text='Hello', bg='white', cursor="exchange").pack()
# b10 = Button(text='Hello', bg='white', cursor="mouse").pack()
# b11 = Button(text='Hello', bg='white', cursor="pirate").pack()
# b12 = Button(text='Hello', bg='white', cursor="plus").pack()
# b13 = Button(text='Hello', bg='white', cursor="shuttle").pack()
# b14 = Button(text='Hello', bg='white', cursor="sizing").pack()
# b15 = Button(text='Hello', bg='white', cursor="spider").pack()
# b16 = Button(text='Hello', bg='white', cursor="spraycan").pack()
# b17 = Button(text='Hello', bg='white', cursor="star").pack()
# b18 = Button(text='Hello', bg='white', cursor="target").pack()
# window.mainloop()

# ---------------------------------------------------------
# window = Tk()
# window.geometry('500x500+500+150')
# window.title('Hello Tkinter')
# b = Button(text='Hello', width=30, height=20, bg='white', fg='red',
#            activebackground='gray', activeforeground='white', bd=30, underline=1).pack()
# window.mainloop()

# -------------------------------------------------------------
# window = Tk()
# window.geometry('600x600+500+150')
# window.title('Hello Tkinter')
# photo = PhotoImage(
#     file=r"/Users/abdelrahmanhossam/Documents/pythonCourse/ball.png")
# b = Button(text='Hello', width=30, height=20, bg='black', fg='red',
#            activebackground='gray', activeforeground='white', bd=30, underline=1, image=photo,
#            highlightthickness=200)
# b.image = photo
# b.pack()
# window.mainloop()
# -------------------------------------------------------------
# window = Tk()
# window.geometry('500x500+500+150')
# window.title('Hello Tkinter')


# def hello():
#     l = Label(text='Hello', fg='#ffffff', bg='#f87217').pack()


# b1 = Button(text='Enter', command=hello, fg='red').pack()

# window.mainloop()
# -------------------------------------------------------------
# window = Tk()
# window.geometry('500x500+500+150')
# window.title('Hello Tkinter')


# def hello():
#     m = b.get()
#     l = Label(text=m, fg='#ffffff', bg='#f87217').pack()


# b = StringVar()
# b1 = Button(text='Enter', command=hello, fg='red').pack()
# text = Entry(textvariable=b).pack()
# window.mainloop()
# -------------------------------------------------------------
# window = Tk()
# window.geometry('500x500+500+150')
# window.title('Hello Tkinter')

# slider = Scale(window, from_=0, to=100)
# slider.set(50)
# slider.pack()

# slider2 = Scale(window, from_=0, to=1000, resolution=0.001)
# slider2.pack()
# window.mainloop()
# -------------------------------------------------------------

# class myFirstGui:
#     def __init__(self, window):
#         self.window = window
#         self.window.title("Hello Tkinter")
#         self.window.geometry('500x500+500+150')

#         self.button1 = Button(text="HI Tkinter", fg='red',
#                               command=self.hi).pack()
#         self.button2 = Button(text="Exit", fg='Blue',
#                               command=window.quit).pack()

#     def hi(self):
#         print("Hello From Python")


# myWindow = Tk()
# my_Gui = myFirstGui(myWindow)
# myWindow.mainloop()
# ---------------------------------------------------------
# window = Tk()
# windowNew = Tk()
# window.geometry('500x500+100+150')
# window.title('Hello Python')
# windowNew.geometry('500x500+700+150')
# windowNew.title('Hello Tkinter')


# def hello():
#     m = b.get()
#     l = Label(text=m, fg='#ffffff', bg='#f87217').pack()


# def good():
#     m = b.get()
#     l = Label( text="Thank You", fg='#f87217', bg='#ffffff').pack()


# b = StringVar()
# b1 = Button(text='Enter', command=hello, fg='red').pack()
# b2 = Button( text='Thanks', command=good, fg='red').pack()
# text = Entry(textvariable=b).pack()
# window.mainloop()
# ---------------------------------------------------------
# window = Tk()
# windowNew = Tk()
# window.geometry('500x500+100+150')
# window.title('Hello Python')
# windowNew.geometry('500x500+700+150')
# windowNew.title('Hello Tkinter')


# def hello():
#     m = b.get()
#     l = Label(text=m, fg='#ffffff', bg='#f87217').pack()


# def good():
#     m = b.get()
#     l = Label(text="Thank You", fg='#f87217', bg='#ffffff').pack()


# b = StringVar()
# b1 = Button(text='Enter', command=hello, fg='red').pack()
# b2 = Button(windowNew, text='Thanks', command=good, fg='red').pack()
# text = Entry(textvariable=b).pack()
# window.mainloop()
# ---------------------------------------------------------
# window = Tk()
# window.geometry('500x500+500+150')
# window.title('Hello Tkinter')
# L = Button(text='Push Here', command=lambda: L.destroy(), fg='red')
# L.pack()
# x = Button(text='quit Here', command=lambda: L.quit(), fg='red')
# x.pack()
# window.mainloop()
# ---------------------------------------------------------
# window = Tk()
# window.geometry('500x500+500+150')
# window.title('Hello Tkinter')


# def show():
#     print(f"Name ==> {e1.get()}, Password ==> {e2.get()}")


# e1 = Entry(window, bg='white', fg='red')
# e2 = Entry(window)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# l1 = Label(text=("Name")).grid(row=0)
# l2 = Label(text=("Password")).grid(row=1)
# L = Button(text='Exit', command=lambda: L.quit(), fg='red')
# L.grid(row=3, column=0)
# x = Button(text='Show Data', command=show, fg='red')
# x.grid(row=3, column=2)
# window.mainloop()
# ---------------------------------------------------------
# window = Tk()
# window.geometry('500x500+500+150')
# window.title('Hello Tkinter')
# window.config(bg="white")
# frame = ttk.Frame(window)
# frame.pack()
# frame.config(height=200, width=400)
# frame.config(relief=RIDGE)
# ttk.Button(frame, text="Frame").pack()
# frame.config(padding=(50, 25))
# ttk.LabelFrame(window, width=400, height=200, text="Labeled Frame").pack()
# window.mainloop()
# ---------------------------------------------------------
# window = Tk()
# window.geometry('500x500+500+150')
# window.title('Hello Tkinter')
# p1 = ttk.Progressbar(window, orient=HORIZONTAL, length=300)
# p1.pack()
# p1.config(maximum=100, value=25)
# p1.start()
# value1 = DoubleVar()
# p1.config(variable=value1)
# scale = ttk.Scale(window, orient=HORIZONTAL, length=250, variable=value1,
#                   from_=0.0, to=100)
# scale.pack()
# window.mainloop()

# ---------------------------------------------------------
# window = Tk()
# window.geometry('250x250+500+150')
# window.title('Hello Tkinter')
# combo1 = ttk.Combobox(window)
# combo1.pack()
# combo1.config(value=("One", "Two", "Three", "Four", "Five",
#               "Six", "Seven", "Eight", "Nine", "Ten"))
# combo1.set("One")
# spin = ttk.Spinbox(window, from_=1990, to=2020,
#                    command=lambda: print(spin.get()))
# spin.pack()

# window.mainloop()
# ---------------------------------------------------------
# window = Tk()
# window.geometry('250x250+500+150')
# window.title('Hello Tkinter')


# def rescall():
#     read = readvar.get()
#     if read == 1:
#         window.configure(background='blue')
#     elif read == 2:
#         window.configure(background='red')
#     elif read == 3:
#         window.configure(background='gold')


# readvar = tk.IntVar()
# red1 = tk.Radiobutton(window, text="Blue", variable=readvar,
#                       value=1, command=rescall)
# red2 = tk.Radiobutton(window, text="Red", variable=readvar,
#                       value=2, command=rescall)
# red3 = tk.Radiobutton(window, text="Gold", variable=readvar,
#                       value=3, command=rescall)
# red1.grid(column=0, row=0)
# red2.grid(column=0, row=1)
# red3.grid(column=0, row=2)

# window.mainloop()
# ---------------------------------------------------------
# window = Tk()
# window.geometry('500x250+500+150')
# window.title('Hello Tkinter')

# note = ttk.Notebook(window)
# tab1 = Frame(window)
# tab2 = Frame(window)
# tab3 = Frame(window)
# ttk.Button(tab1, text="Exit", command=window.destroy).pack()

# note.add(tab1, text="Tab One")
# note.add(tab2, text="Tab Two")
# note.add(tab3, text="Tab Three")
# note.pack()

# window.mainloop()
