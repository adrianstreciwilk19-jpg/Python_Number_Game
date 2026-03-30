import random

print("Witaj w grze 'Zgadnij Liczbę'!")
print("Wylosowana zostanie losowa liczba z zakresu od 0 do 1000. Twoim zadaniem jest odgadnąć tę liczbę.")
print("Po każdej próbie otrzymasz wskazówkę, czy Twoja liczba jest za duża lub za mała.")
ready = input("Czy jesteś gotowy? (T/N): ")

try:
    with open("gr.txt", "r") as p:
        ver = p.read()

except FileNotFoundError:
    with open("gr.txt", "w") as w:
        w.write("0")
    ver = "0"

    if not ver.isdecimal():
        with open("gr.txt", "w") as w:
            w.write("0")


if ready.lower() == 't':

    while True:
        number = random.randint(0, 1000)

        print("Liczba została wylosowana. Zacznij rozgrywkę!")

        attempt = 0

        while True:
            win = " "
            attempt = attempt + 1

            attempt = int(attempt)
            #print(attempt)
            #output do debugowania
            #print(number)

            guess = input("Podaj swoją liczbę: ")

            if guess.lower().strip() == "stop":           
                break
            elif not guess.isdecimal():
                print("Podany znak nie jest liczbą")
                guess = input("Podaj swoją liczbę ponownie: ")
                guess = int(guess)
            else: 
                guess = int(guess)


            guess = int(guess)
            if guess > number:
                print("Wylosowana liczba jest mniejsza od podanej.")
            elif guess < number:
                print("Wylosowana liczba jest większa od podanej.")
            else:
                print("Brawo! Podana liczba jest taka sama jak liczba wylosowana!")
                print("Udało Ci się odgadnąć liczbę w ", attempt, " prób!")
                win = "T"
                with open("gr.txt", "r") as f:
                    gr = f.read()
                    gr = int(gr)
                if attempt < gr or gr == 0:
                    with open("gr.txt", "w") as h:
                        h.write(str(attempt))
                    print("Dotychczasowy rekord to ", gr, "prób, udało Ci się go pobić. Gratulacje!")
                else:
                    print("Dotychczasowy rekord to ", gr, "prób, niestety nie udało Ci się go pobić.")

            if win == "T":
                ready = input("Czy chcesz zagrać ponownie? (T/N)")
                break

        if ready.lower() != 't':
            print("Dziękujemy za rozgrywkę :)")
            break
        









        

