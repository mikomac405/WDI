from tkinter import *
import tkinter
import random

def prt():
    def reset1():
        twoja.destroy()
        los.destroy()
        less.destroy()
        line.destroy()
        button2.destroy()
        prt()

    def reset2():
        twoja.destroy()
        los.destroy()
        more.destroy()
        line.destroy()
        button2.destroy()
        prt()

    def reset3():
        twoja.destroy()
        los.destroy()
        win.destroy()
        line.destroy()
        button2.destroy()
        prt()

    frombox = int(box.get())
    liczba = random.randint(1, 100)

    twoja = Label(S, text=("Twoja liczba: " + str(frombox)))
    twoja.pack()

    los = Label(S, text=("Wylosowana liczba: " + str(liczba)))
    los.pack()

    if frombox < liczba:
        less = Label(S, text="za mała liczba")
        less.pack()
        line = Label(S, text="============")
        line.pack()

        button.destroy()

        button2 = tkinter.Button(S, text="Spróbuj jeszcze raz!", command=reset1)
        button2.pack()

    if frombox > liczba:
        more = Label(S, text="za duża liczba")
        more.pack()
        line = Label(S, text="============")
        line.pack()

        button.destroy()

        button2 = tkinter.Button(S, text="Spróbuj jeszcze raz!", command=reset2)
        button2.pack()

    if frombox == liczba:
        win = Label(S, text="brawo, mój przyjacielu")
        win.pack()
        line = Label(S, text="============")
        line.pack()

        button.destroy()

        button2 = tkinter.Button(S, text="Spróbuj jeszcze raz!", command=reset3)
        button2.pack()

S = Tk()
S.title("Moduł I, temat 8")

wpis = Label(S, text="Wpisz liczbe")
wpis.pack()

box = Entry(S, bd=5)
box.pack()

button = tkinter.Button(S, text="Sprawdź czy trafiłeś!", command=prt)
button.pack()

S.mainloop()

