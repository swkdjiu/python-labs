from models import Book, EBook, Member
from logic import Library

def main():
   
    moja_biblioteka = Library()

    
    ksiazka1 = Book("Wiedźmin", "Andrzej Sapkowski", 1992, "101")
    ksiazka2 = Book("Hobbit", "J.R.R. Tolkien", 1937, "102")
    ksiazka3 = Book("Diuna", "Frank Herbert", 1965, "103")

    ebook1 = EBook("Python Crash Course", "Eric Matthes", 2019, "E01", "pdf")
    ebook2 = EBook("Czysty Kod", "Robert C. Martin", 2008, "E02", "epub")

   
    moja_biblioteka.add_book(ksiazka1)
    moja_biblioteka.add_book(ksiazka2)
    moja_biblioteka.add_book(ksiazka3)
    moja_biblioteka.add_book(ebook1)
    moja_biblioteka.add_book(ebook2)

    
    imiona = ["Anna Nowak", "Piotr Zieliński", "Katarzyna Woźniak", "Michał Lewandowski"]
    for i, imie in enumerate(imiona, start=1):
        nowy_czlonek = Member(imie, i)
        moja_biblioteka.register_member(nowy_czlonek)

    while True:
        print("\n--- SYSTEM BIBLIOTECZNY ---")
        print("1. Pokaż wszystkie książki")
        print("2. Wypożycz książkę")
        print("3. Zwróć książkę")
        print("4. Szukaj po tytule")
        print("5. Szukaj po autorze")
        print("6. Dodaj nową książkę")      
        print("7. Zarejestruj czytelnika")  
        print("8. Wyjście")
        
        wybor = input("\nWybierz opcję (1-8): ")

        if wybor == "1":
            print("\nKatalog książek:")
            for k in moja_biblioteka.ksiazki:
                print(k)

        elif wybor == "2":
            try:
                m_id = int(input("Podaj ID użytkownika: "))
                isbn = input("Podaj ISBN książки: ")
                if moja_biblioteka.borrow(m_id, isbn):
                    print(">>> Sukces!")
                else:
                    print(">>> Błąd: Książka zajęta lub złe dane.")
            except ValueError:
                print(">>> Błąd: ID musi być liczbą!")

        elif wybor == "3":
            # Тут код для возврата (как у тебя был)
            m_id = int(input("Podaj ID użytkownika: "))
            isbn = input("Podaj ISBN książki: ")
            moja_biblioteka.return_book(m_id, isbn)
            print(">>> Książka zwrócona.")

        elif wybor == "4":
            fraza = input("Wpisz tytuł lub jego część: ")
            wyniki = moja_biblioteka.search_by_title(fraza)
            print(f"Znaleziono ({len(wyniki)}):")
            for w in wyniki: print(w)

        elif wybor == "5": 
            autor_fraza = input("Wpisz nazwisko autora: ")
            wyniki = moja_biblioteka.search_by_autor(autor_fraza)
            print(f"Książki autora {autor_fraza} ({len(wyniki)}):")
            for w in wyniki: 
                print(w)

        elif wybor == "6":
            print("\n--- Dodawanie nowej książki ---")
            tytul = input("Tytuł: ")
            autor = input("Autor: ")
            rok = int(input("Rok wydania: "))
            isbn = input("ISBN: ")
            
            typ = input("Czy to e-book? (t/n): ").lower()
            if typ == 't':
                fmt = input("Format (pdf/epub): ")
                nowa_ksiazka = EBook(tytul, autor, rok, isbn, fmt)
            else:
                nowa_ksiazka = Book(tytul, autor, rok, isbn)
            
            moja_biblioteka.add_book(nowa_ksiazka)
            print(">>> Książka dodana do systemu!")

        elif wybor == "7":
            print("\n--- Rejestracja nowego członka ---")
            imie = input("Imię i nazwisko: ")
            nowy_id = len(moja_biblioteka.czlonkowie) + 1
            
            nowy_m = Member(imie, nowy_id)
            moja_biblioteka.register_member(nowy_m)
            print(f">>> Zarejestrowano: {imie} (Twoje ID to: {nowy_id})")

        elif wybor == "8":
            print("Zamykanie systemu. Do widzenia!")
            break

if __name__ == "__main__":
    main()