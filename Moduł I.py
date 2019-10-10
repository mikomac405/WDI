from tkinter import *
from keyboard import press
import tkinter
import random


def esc():
    S.destroy()


def prt():
    global a, b, c, x, liczba

    def reset():
        global a, b, c, x, liczba
        twoja.destroy()


        if a == 1:
            less.destroy()
            a = 0
        if b == 1:
            more.destroy()
            b = 0
        if c == 1:
            button3.destroy()
            win.destroy()
            liczba = random.randint(1, 100)
            c = 0
            x = -1

        line.destroy()
        proby.destroy()
        button2.destroy()
        prt()

    if box.get().isdigit():
        if int(box.get()) < 0 or int(box.get()) > 100:
            frombox = 0
        else:
            frombox = int(box.get())
    else:
        frombox = 0

    box.delete(0, 'end')

    twoja = Label(S, text=("Twoja liczba: " + str(frombox)))
    twoja.pack()

    if frombox < liczba:
        less = Label(S, text="za mała liczba", fg="red")
        less.pack()
        a = 1
        x += 1

    if frombox > liczba:
        more = Label(S, text="za duża liczba", fg="red")
        more.pack()
        b = 1
        x += 1

    if frombox == liczba:
        win = Label(S, text="brawo, mój przyjacielu", fg="orange")
        win.pack()
        c = 1
        x += 1

    if c == 1:
        proby = Label(S, text="Ilość prób: "+str(x))
    else:
        proby = Label(S, text="Ilość prób: " + str(x), fg="green")

    proby.pack()
    line = Label(S, text="============")
    line.pack()

    button.destroy()

    if c == 1:
        button3 = tkinter.Button(S,text="Zakończ grę", bg="red", command=esc)
        button3.pack()

    button2 = tkinter.Button(S, text="Spróbuj jeszcze raz!", command=reset)
    button2.pack()


S = Tk()
S.title("Moduł I, temat 8")
a = 0
b = 0
c = 0
x = 0

liczba = random.randint(1, 100)

wpis = Label(S, text="Wpisz liczbe")
wpis.pack()

box = Entry(S, bd=5)
box.pack()

button = tkinter.Button(S, text="Sprawdź czy trafiłeś!", command=prt)
button.pack()

S.mainloop()
