from models import inicjalizuj_dane, zapisz_dane
from actions import dodaj_wydatek, oblicz_sumę
import logging

def main():
    dane = inicjalizuj_dane()

    while True:
        print("1.Dodaj | 2.Statystyki | 3.Wyjście")
        wybor = input("Wybierz: ")
        
        if wybor == "1":
            dodaj_wydatek(dane)
            zapisz_dane(dane)
        elif wybor == "2":
            oblicz_sumę(dane)
        elif wybor == "3":
            logging.info("Koniec pracy.")
            break
        else:
            logging.warning("Nieznany błąd")

if __name__  == '__main__':
    main()
