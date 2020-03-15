from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

Trening = {
     "Noge":[
       """      Čučanj: 10 ponavljanja, 3 seta, odmor: 90 sec \n
        Leg Extension: 10 ponavljanja, 3 seta, odmor: 90 sec \n
        Leg Press: 12 ponavljanja, 3 seta, odmor: 90 sec \n
        Leg Curl: 12 ponavljanja,3 seta, odmor: 70 sec \n 
        DB Lunges: 14 ponavljanja, 3 seta, odmor: 70 sec"""
],
    "Sisice":[
       """      Incline BB press: 8 ponavljanja, 3 seta, odmor: 90 sec\n
       Flat DB press: 10 ponavljanja, 3 seta, odmor 90sec \n
       Seated DB shoulder press: 8 ponavljanja, 3 seta, odmor: 90 sec\n
       Cable fly: 10 ponavljanja, 3 seta, odmor: 90 sec\n
       [Overhead tricep DB extension: 8 ponavljanja, 3 seta, odmor: 80 sec + 
       Seated DB lateral raise: 12 ponavljanja, 3 seta, odmor: 80 sec]\n
       Lying EZ skull crushers: 10 ponavljanja, 3 seta, odmor: 80 sec\n
       Tricep cable pressdown: 12 ponavljanja, 3 seta, odmor: 80 sec"""
  ],
    "Leda":[
        """     Mrtva dizanja: 10 ponavljanja, 3 seta, odmor: 90 sec\n
        Chin up (neutral grip): 6-10 ponavljanja, 3 serije, odmor: 120sec\n 
        Lat pulldown: 10 ponavljanja, 3 serije, odmor 90sec\n
        One arm DB row: 10 ponavljanja, 3 serije, odmor 70sec\n
        Standing BB curls:  8 ponavljanja, 3 serije, odmor 80sec\n
        Standing BB shrugs: 8 ponavljanja, 3 serije, odmor 70sec\n
        [Incline DB hammer curls: 10 ponavljanja, 3 serije, odmor 90sec + 
        DB rear delt fly: 12 ponavljanja, 3 serije, odmor 90sec]\n
        Single arm DB preacher curls: 10 ponavljanja, 3 serije, odmor 70sec"""
    ]
}
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
