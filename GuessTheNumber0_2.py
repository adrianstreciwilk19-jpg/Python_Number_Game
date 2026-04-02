import random
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

#konfiguracja logów
def configure_logger():
    #utworzenie pliku w folderze aplikacji
    log_dir = Path(__file__).parent
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / 'app.log'

    #Nadanie identyfikatora logów
    logger = logging.getLogger('GuessTheNumber')

    #nadanie minimalnego poziomu logów
    logger.setLevel(logging.INFO)

    #sprawdzenie czy logger ma juz przypisane handlery
    if logger.handlers:
        return logger

    #format logów
    formatter = logging.Formatter(
        fmt="%(asctime)s|%(levelname)s|%(name)s[%(message)s]",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    #konfiguracja pliku logów, po osiągnięciu 1mb tworzony jest nowy plik do max 3 plików archiwalnych 
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=1_000_000, #1MB
        backupCount=3,
        encoding='utf-8'
    )
    #poziom logowania
    file_handler.setLevel(logging.INFO)
    #format loga
    file_handler.setFormatter(formatter)

    #podpięcie handlera do loggera
    logger.addHandler(file_handler)

    return logger

#przypisanie do zmiennej logger konfiguracji loggera
logger = configure_logger()

#logowanie
logger.info("Start aplikacji")

#Opis funkcjonalności
print("Witaj w grze 'Zgadnij Liczbę'!")
print("Wylosowana zostanie losowa liczba z zakresu od 0 do 1000. Twoim zadaniem jest odgadnąć tę liczbę.")
print("Po każdej próbie otrzymasz wskazówkę, czy Twoja liczba jest za duża lub za mała.")
#Input rozpoczynający grę
ready = input("Czy jesteś gotowy? (T/N): ")


file_path = Path(__file__).parent / "gr.txt"

#Sprawdzenie czy istnieje plik z rekordem gry "gr.txt"
try:
    with open(file_path, "r") as p:
        ver = p.read()
        logger.info("Odczytanie wartości z pliku gr.txt")

#Jeżeli nie istnieje dostajemy błąd, który wywołuje funkcję tworzenia pliku
except FileNotFoundError:
    with open(file_path, "w") as w:
        w.write("0")
    ver = "0"
    logger.warning("Brak pliku gr.txt, plik został utworzony")
#Weryfikacja czy wartość odczytana z pliku jest liczbą
    if not ver.isdecimal():
        with open(file_path, "w") as w:
            w.write("0")
        logger.warning("Wartość z pliku gr.txt nie była liczbą, zapisano 0")


if ready.lower() == 't':
    logger.info("Użytkownik rozpoczął grę")

    #Pętla zawierająca logikę gry
    while True:
        #Utworzenie zmiennych, losowanie liczby, rozpoczęcie gry
        number = random.randint(0, 1000)
        print("Liczba została wylosowana. Zacznij rozgrywkę!")
        logger.info(f"Wylosowano liczbę {number}")
        attempt = 0

        #Pętla gry
        while True:

            #Nadanie zmiennych, input podania liczby
            win = " "
            attempt = attempt + 1
            attempt = int(attempt)
            guess = input("Podaj swoją liczbę: ")
            logger.info(f"Użytkownik podał liczbę {guess}")

            #Weryfikacja poprawności wpisanej liczby oraz ewentualnego zatrzymania gry
            if guess.lower().strip() == "stop":     
                ready = 'N'      
                logger.info("Użytkownik zarządał zatrzymania rozgrywki")
                break
            elif not guess.isdecimal():
                logger.warning("Użytkownik nie podał liczby")
                print("Podany znak nie jest liczbą")
                guess = input("Podaj swoją liczbę ponownie: ")
                while not guess.isdecimal():
                    logger.error("Użytkownik ponownie nie podał liczby")
                    print("Podany znak nie jest liczbą")
                    guess = input("Podaj swoją liczbę ponownie: ")
                    if guess.lower().strip() == "stop":
                        ready = 'N'      
                        logger.info("Użytkownik zarządał zatrzymania rozgrywki")
                        print("Dziękujemy za rozgrywkę :)")
                        exit()
                guess = int(guess)
                
            else: 
                guess = int(guess)
                

            #Weryfikacja czy podana liczba jest większa, mniejsza lub równa wylosowanej
            if guess > number:
                print("Wylosowana liczba jest mniejsza od podanej.")
                logger.info(f"Liczba wylosowana {number} jest mniejsza od wybranej {guess}")
            elif guess < number:
                print("Wylosowana liczba jest większa od podanej.")
                logger.info(f"Liczba wylosowana {number} jest większa od wybranej {guess}")
            else:
                #Jeżeli liczba jest równa wylosowanej gra zostaje ukończona i podane zostaje ile prób użytkownikowi zajęło ukończenie oraz jaki był rekord i czy był
                print("Brawo! Podana liczba jest taka sama jak liczba wylosowana!")
                print("Udało Ci się odgadnąć liczbę w ", attempt, " prób!")
                logger.info("Użytkownik odgadł liczbę")
                win = "T"
                with open(file_path, "r") as f:
                    gr = f.read()
                    gr = int(gr)
                    logger.info("Odczytanie rekordu z pliku gr.txt")
                if attempt < gr:
                    with open(file_path, "w") as h:
                        h.write(str(attempt))
                    print("Dotychczasowy rekord to", gr, "prób, udało Ci się go pobić. Gratulacje!")
                    logger.info("Użytkownik pobił rekord zapisany w pliku gr.txt")
                elif gr == 0:
                    with open(file_path, "w") as h:
                        h.write(str(attempt))
                    print("Jesteś pierwszy, Twój wynik oraz aktualny rekord to:", attempt, " prób!")
                    logger.info("Użytkownik po raz pierwszy ustanowił swój rekord")
                else:
                    print("Dotychczasowy rekord to", gr, "prób, niestety nie udało Ci się go pobić.")
                    logger.info("Użytkownik nie pobił swojego reordu")
                    
            #Weryfikacja czy użytkownik chce zagrać ponownie
            if win == "T":
                ready = input("Czy chcesz zagrać ponownie? (T/N)")
                break

        #Przerwanie gry jeżeli użytkownik nie zdecydował się kontynuuować
        if ready.lower() != 't':
            print("Dziękujemy za rozgrywkę :)")
            logger.info("Użytkownik postanowił przerwać rogrywkę")
            break
        logger.info("Użytkownik zdecydował się kontynuuować rozgrywkę")









        

