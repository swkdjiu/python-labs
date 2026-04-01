from models import Book, Member

class Library:
    def __init__(self):
        self.ksiazki = []
        self.czlonkowie = []

    def add_book(self, ksiazka: Book):
        self.ksiazki.append(ksiazka)

    def register_member(self, czlonek: Member):
        self.czlonkowie.append(czlonek)

    def borrow(self, member_id: int, isbn: str):
        # 1. Szukamy osoby
        osoba = None
        for m in self.czlonkowie:
            if m.id == member_id:
                osoba = m
                break  

        # 2. Szukamy książki
        ksiazka = None
        for k in self.ksiazki:
            if k.isbn == isbn:
                ksiazka = k
                break

        # 3. Logika 
        if osoba and ksiazka and ksiazka.dostepnosc:
            ksiazka.dostepnosc = False  # Zmieniamy status na niedostępny
            osoba.wypozyczone_ksiazki.append(ksiazka) # Dodajemy do listy usera
            return True # Udało się
            
        return False # Coś poszło nie tak (brak osoby, książki lub już zajęta)
    
    def return_book(self, member_id: int, isbn: str):

        osoba = None
        for m in self.czlonkowie:
            if m.id == member_id:
                osoba = m
                break

        if not osoba:
            print("Nie znaleziono takiego czytelnika.")
            return False

        ksiazka_do_zwrotu = None
        for k in osoba.wypozyczone_ksiazki:
            if k.isbn == isbn:
                ksiazka_do_zwrotu = k
                break

        if ksiazka_do_zwrotu:
            ksiazka_do_zwrotu.dostepnosc = True 
            osoba.wypozyczone_ksiazki.remove(ksiazka_do_zwrotu) 
            print(f"Książka '{ksiazka_do_zwrotu.tytul}' została zwrócona.")
            return True
        
        print("Ten czytelnik nie ma takiej książki.")
        return False
    
    def search_by_title(self, tytul: str):
        znalezione = []
        for k in self.ksiazki:
            if tytul.lower() in k.tytul.lower():
                znalezione.append(k)
        return znalezione

    def search_by_autor(self, autor: str):
        znalezione = []
        for k in self.ksiazki:
            if autor.lower() in k.autor.lower():
                znalezione.append(k)
        return znalezione