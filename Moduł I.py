import tkinter
from tkinter import *
import random


def check():
    global success, try_count, random_number

    def reset():
        global success, try_count, random_number

        if 'less_label' in locals():
            less_label.destroy()
        if 'more_label' in locals():
            more_label.destroy()
        if success == 1:
            quit_button.destroy()
            win_label.destroy()
            random_number = random.randint(1, 100)
            success = False
            try_count = -1

        try_label.destroy()
        feedback.destroy()
        retry_button.destroy()
        check()

    if box.get().isdigit():
        if int(box.get()) < 0 or int(box.get()) > 100:
            box_input = -1
            feedback = Label(Okno, text="Twoja liczba musi zawierać się \n w przedziale od 0 do 100.")
        else:
            box_input = int(box.get())
            feedback = Label(Okno, text="Twoja liczba: " + str(box_input))
    else:
        box_input = -1
        feedback = Label(Okno, text="Możesz wpisywać tylko liczby")

    box.delete(0, 'end')
    feedback.pack()

    if box_input < random_number:
        less_label = Label(Okno, text="za mała liczba", fg="red")
        less_label.pack()
        try_count += 1

    if box_input > random_number:
        more_label = Label(Okno, text="za duża liczba", fg="red")
        more_label.pack()
        try_count += 1

    if box_input == random_number:
        win_label = Label(Okno, text="brawo, mój przyjacielu", fg="orange")
        win_label.pack()
        success = True
        try_count += 1

    try_label = Label(Okno, text="Ilość prób: " + str(try_count), fg="green")
    try_label.pack()

    check_button.destroy()

    if success:
        quit_button = tkinter.Button(Okno, text="Zakończ grę", bg="red", command=esc)
        quit_button.pack()

    retry_button = tkinter.Button(Okno, text="Spróbuj jeszcze raz!", command=reset)
    retry_button.pack()


def esc():
    Okno.destroy()


success = 0
try_count = 0
random_number = random.randint(1, 100)

Okno = Tk()
Okno.title("Moduł I, temat 8")

task = Label(Okno, text="Wpisz liczbe")
task.pack()

box = Entry(Okno, bd=5)
box.pack()

check_button = tkinter.Button(Okno, text="Sprawdź czy trafiłeś!", command=check)
check_button.pack()

Okno.mainloop()
