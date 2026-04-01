import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from logic import Library
from models import Book, Member

# --- FIXTURE (Odpowiednik setUp) ---
@pytest.fixture
def library():
    """Tworzy testową bibliotekę z przykładowymi danymi przed każdym testem."""
    lib = Library()
    
    # Dodajemy książkę
    ksiazka = Book("Wiedźmin", "Andrzej Sapkowski", 1992, "101")
    lib.add_book(ksiazka)
    
    # Rejestrujemy członka
    czlonek = Member("Anna Nowak", 1)
    lib.register_member(czlonek)
    
    return lib

#  TESTY WYPOŻYCZANIA 

def test_borrow_success(library):
    """Test udanego wypożyczenia (przypadek sukcesu)."""
    # Próba wypożyczenia: ID=1, ISBN='101'
    result = library.borrow(1, "101")
    
    assert result is True
    # Sprawdzamy, czy status książki w bibliotece zmienił się na False
    assert library.ksiazki[0].dostepnosc is False
    # Sprawdzamy, czy książka trafiła na listę użytkownika
    assert len(library.czlonkowie[0].wypozyczone_ksiazki) == 1

def test_borrow_fail_already_borrowed(library):
    """Test błędu, gdy książka jest już niedostępna."""
    # Pierwsze wypożyczenie (sukces)
    library.borrow(1, "101")
    
    # Druga próba wypożyczenia tej samej książki (powinna zwrócić False)
    result = library.borrow(1, "101")
    
    assert result is False

def test_borrow_fail_wrong_data(library):
    """Test błędu przy błędnych danych (złe ID lub ISBN)."""
    assert library.borrow(999, "101") is False  # Nieistniejący użytkownik
    assert library.borrow(1, "999") is False    # Nieistniejący ISBN

# --- TESTY WYSZUKIWANIA ---

def test_search_by_title_found(library):
    """Test wyszukiwania po tytule (przypadek znalezienia)."""
    wyniki = library.search_by_title("Wiedź")
    assert len(wyniki) == 1
    assert wyniki[0].tytul == "Wiedźmin"

def test_search_by_title_not_found(library):
    """Test wyszukiwania po tytule (brak wyników)."""
    wyniki = library.search_by_title("Harry Potter")
    assert len(wyniki) == 0

def test_search_by_autor(library):
    """Test wyszukiwania po autorze."""
    wyniki = library.search_by_autor("Sapkowski")
    assert len(wyniki) == 1
    assert "Wiedźmin" in wyniki[0].tytul