from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from trening import *


def hide_me(self, event):
    print('hide me')
    event.widget.place_forget()

def callback():
    label = Label(window, text=Trening.get("Noge"), font=("Arial Bold", 13), foreground = 'blue')
    label.pack()


def callback1():
    label = Label(window, text=Trening.get("Sisice"), font=("Arial Bold", 13), foreground = 'purple')
    label.pack()

def callback2():
    label = Label(window, text=Trening.get("Leda"), font=("Arial Bold", 13), foreground = 'orange')
    label.pack()

window = Tk()

window.title("Trening")

style = Style()
style.configure('TButton', font =
               ('calibri', 10, 'bold'),
                foreground = 'green')

b = ttk.Button(window, text="Noge")
b.config(command=callback)

b.pack()


b1 = ttk.Button(window, text="Prsa")
b1.config(command=callback1)
b1.pack()

b2 = ttk.Button(window, text="Leđa")
b2.config(command=callback2)
b2.pack()


window.mainloop()


#x = input("Unesi koji trening želiš: ")
#print(Trening.get(x))
