import random

random_number = random.randint(1, 100)
print(random_number)
guess_number = 0
while guess_number is not random_number:
    guess_number = int(input("Podaj liczbę: "))
    if guess_number < random_number:
        print("za mała liczba")
    else:
        print("za duża liczba")
print("brawo, mój przyjacielu")
stop = input("Wcisnij enter, aby zakończyć")
