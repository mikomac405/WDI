import random

rand = random.randint(1,100)
print(rand)
liczba = 0
while liczba != rand:
    liczba = int(input("Podaj liczbę: "))
    if liczba < rand :
        print("za mała liczba")
    if liczba > rand :
        print("za duża liczba")
print("brawo, mój przyjacielu")
stop = input("Wcisnij enter, aby zakończyć")
