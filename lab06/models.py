from dataclasses import dataclass
from typing import List

@dataclass
class Book:
    tytul: str
    autor: str
    rok: int
    isbn: str
    dostepnosc: bool = True

    def __str__(self):
        status = "Dostępna" if self.dostepnosc else "Wypożyczona"
        return f"'{self.tytul}' - {self.autor} ({self.rok}) [{status}]"

@dataclass
class EBook(Book):

    format_pliku: str = "pdf"
    def __str__(self):
        return super().__str__() + f" [E-book: {self.format_pliku}]"

class Member:
    def __init__(self, imie: str, member_id: int):
        self.imie = imie
        self.id = member_id
        self.wypozyczone_ksiazki: List[Book] = []

    def __str__(self):
        return f"Czytelnik: {self.imie} (ID: {self.id})"
    