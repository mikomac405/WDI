from tkinter import *
import tkinter
import random

def prt():
    global x
    def reset1():
        twoja.destroy()
        less.destroy()
        line.destroy()
        proby.destroy()
        button2.destroy()
        prt()

    def reset2():
        twoja.destroy()
        more.destroy()
        line.destroy()
        proby.destroy()
        button2.destroy()
        prt()

    def reset3():
        twoja.destroy()
        win.destroy()
        line.destroy()
        proby.destroy()
        button2.destroy()
        prt()

    frombox = int(box.get())

    box.delete( 0,'end')

    twoja = Label(S, text=("Twoja liczba: " + str(frombox)))
    twoja.pack()

    if frombox < liczba:
        less = Label(S, text="za mała liczba")
        less.pack()
        x+=1

        proby= Label(S, text="Ilość prób: "+str(x))
        proby.pack()
        line = Label(S, text="============")
        line.pack()

        button.destroy()

        button2 = tkinter.Button(S, text="Spróbuj jeszcze raz!", command=reset1)
        button2.pack()

    if frombox > liczba:
        more = Label(S, text="za duża liczba")
        more.pack()
        x+=1

        proby= Label(S, text="Ilość prób: "+str(x))
        proby.pack()
        line = Label(S, text="============")
        line.pack()

        button.destroy()

        button2 = tkinter.Button(S, text="Spróbuj jeszcze raz!", command=reset2)
        button2.pack()

    if frombox == liczba:
        win = Label(S, text="brawo, mój przyjacielu")
        win.pack()
        x+=1

        proby= Label(S, text="Ilość prób: "+str(x))
        proby.pack()
        line = Label(S, text="============")
        line.pack()

        button.destroy()

        button2 = tkinter.Button(S, text="Spróbuj jeszcze raz!", command=reset3)
        button2.pack()

S = Tk()
S.title("Moduł I, temat 8")

x = 0

liczba = random.randint(1, 100)

wpis = Label(S, text="Wpisz liczbe")
wpis.pack()

box = Entry(S, bd=5)
box.pack()

button = tkinter.Button(S, text="Sprawdź czy trafiłeś!", command=prt)
button.pack()

S.mainloop()

