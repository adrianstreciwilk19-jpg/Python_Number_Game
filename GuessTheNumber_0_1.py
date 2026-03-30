import random

#Opis funkcjonalności
print("Witaj w grze 'Zgadnij Liczbę'!")
print("Wylosowana zostanie losowa liczba z zakresu od 0 do 1000. Twoim zadaniem jest odgadnąć tę liczbę.")
print("Po każdej próbie otrzymasz wskazówkę, czy Twoja liczba jest za duża lub za mała.")
#Input rozpoczynający grę
ready = input("Czy jesteś gotowy? (T/N): ")

#Sprawdzenie czy istnieje plik z rekordem gry "gr.txt"
try:
    with open("gr.txt", "r") as p:
        ver = p.read()

#Jeżeli nie istnieje dostajemy błąd, który wywołuje funkcję tworzenia pliku
except FileNotFoundError:
    with open("gr.txt", "w") as w:
        w.write("0")
    ver = "0"
#Weryfikacja czy wartość odczytana z pliku jest liczbą
    if not ver.isdecimal():
        with open("gr.txt", "w") as w:
            w.write("0")


if ready.lower() == 't':

    #Pętla zawierająca logikę gry
    while True:
        #Utworzenie zmiennych, losowanie liczby, rozpoczęcie gry
        number = random.randint(0, 1000)
        print("Liczba została wylosowana. Zacznij rozgrywkę!")
        attempt = 0

        #Pętla gry
        while True:

            #Nadanie zmiennych, input podania liczby
            win = " "
            attempt = attempt + 1
            attempt = int(attempt)
            guess = input("Podaj swoją liczbę: ")

            #Weryfikacja poprawności wpisanej liczby oraz ewentualnego zatrzymania gry
            if guess.lower().strip() == "stop":           
                break
            elif not guess.isdecimal():
                print("Podany znak nie jest liczbą")
                guess = input("Podaj swoją liczbę ponownie: ")
                guess = int(guess)
            else: 
                guess = int(guess)

            #Weryfikacja czy podana liczba jest większa, mniejsza lub równa wylosowanej
            if guess > number:
                print("Wylosowana liczba jest mniejsza od podanej.")
            elif guess < number:
                print("Wylosowana liczba jest większa od podanej.")
            else:
                #Jeżeli liczba jest równa wylosowanej gra zostaje ukończona i podane zostaje ile prób użytkownikowi zajęło ukończenie oraz jaki był rekord i czy był
                print("Brawo! Podana liczba jest taka sama jak liczba wylosowana!")
                print("Udało Ci się odgadnąć liczbę w ", attempt, " prób!")
                win = "T"
                with open("gr.txt", "r") as f:
                    gr = f.read()
                    gr = int(gr)
                if attempt < gr:
                    with open("gr.txt", "w") as h:
                        h.write(str(attempt))
                    print("Dotychczasowy rekord to", gr, "prób, udało Ci się go pobić. Gratulacje!")
                elif gr == 0:
                    with open("gr.txt", "w") as h:
                        h.write(str(attempt))
                    print("Jesteś pierwszy, Twój wynik oraz aktualny rekord to:", attempt, " prób!")
                else:
                    print("Dotychczasowy rekord to", gr, "prób, niestety nie udało Ci się go pobić.")
                    
            #Weryfikacja czy użytkownik chce zagrać ponownie
            if win == "T":
                ready = input("Czy chcesz zagrać ponownie? (T/N)")
                break

        #Przerwanie gry jeżeli użytkownik nie zdecydował się kontynuuować
        if ready.lower() != 't':
            print("Dziękujemy za rozgrywkę :)")
            break
          
