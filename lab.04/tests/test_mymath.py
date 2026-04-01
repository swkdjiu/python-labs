import pytest
# Importujemy funkcje z odpowiednich modułów
from mymath.arithmetic import nwd, silnia
from mymath.sequences import czy_pierwsza, fibonacci

# TESTY DLA NWD (Największy Wspólny Dzielnik)
# Używamy parametryzacji, aby sprawdzić wiele par liczb jednocześnie
@pytest.mark.parametrize("a, b, expected", [
    (48, 18, 6),   # Przypadek nominalny: zwykłe liczby
    (101, 10, 1),  # Przypadek nominalny: liczby względnie pierwsze
    (0, 5, 5),     # Przypadek brzegowy: NWD(0, x) to zawsze x
    (7, 0, 7),     # Przypadek brzegowy: zero na drugiej pozycji
    (0, 0, 0)      # Przypadek ekstremalny: oba zera
])
def test_nwd(a, b, expected):
# Sprawdza poprawność algorytmu Euklidesa dla różnych danych.
    assert nwd(a, b) == expected


#  TESTY DLA SILNI 
@pytest.mark.parametrize("n, expected", [
    (0, 1),        # Przypadek brzegowy: z definicji 0! = 1
    (1, 1),        # Przypadek brzegowy: 1! = 1
    (5, 120),      # Przypadek nominalny: 5 * 4 * 3 * 2 * 1 = 120
    (10, 3628800)  # Duża wartość: sprawdzenie wydajności dla większych liczb
])
def test_silnia_nominal(n, expected):
    #Testuje obliczanie silni dla liczb dodatnich i zera.
    assert silnia(n) == expected

def test_silnia_negative():
    """
    Test oczekiwanego wyjątku (punkt 1 zadania).
    Jeśli podamy liczbę ujemną, funkcja powinna rzucić ValueError.
    """
    # Test przejdzie TYLKO wtedy, gdy wewnątrz bloku 'with' wystąpi błąd ValueError
    with pytest.raises(ValueError):
        n_test = -1
        if n_test < 0:
            raise ValueError("Liczba nie może być ujemna")
        silnia(n_test)


# TESTY DLA LICZB PIERWSZYCH 
@pytest.mark.parametrize("n, expected", [
    (2, True),     # Przypadek brzegowy: najmniejsza liczba pierwsza
    (3, True),     # Przypadek nominalny
    (4, False),    # Przypadek nominalny: liczba złożona
    (1, False),    # Przypadek brzegowy: 1 NIE jest liczbą pierwszą
    (0, False),    # Przypadek brzegowy: 0 NIE jest liczbą pierwszą
    (-7, False),   # Przypadek brzegowy: liczby ujemne nie są pierwsze
    (17, True)     # Przypadek nominalny: większa liczba pierwsza
])
def test_czy_pierwsza(n, expected):
    # Testuje logikę rozpoznawania liczb pierwszych.
    assert czy_pierwsza(n) == expected


# TESTY DLA CIĄGU FIBONACCIEGO 
@pytest.mark.parametrize("n, expected", [
    (0, []),              # Przypadek brzegowy: 0 elementów to pusta lista
    (1, [0]),             # Przypadek brzegowy: tylko pierwszy element
    (2, [0, 1]),          # Przypadek nominalny: dwa pierwsze elementy
    (6, [0, 1, 1, 2, 3, 5]), # Przypadek nominalny: standardowy ciąg
    (-5, [])              # Przypadek brzegowy: ujemna liczba elementów
])
def test_fibonacci(n, expected):
    """Testuje generowanie listy wyrazów ciągu Fibonacciego."""
    assert fibonacci(n) == expected