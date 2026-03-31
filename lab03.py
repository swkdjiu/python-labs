
# Biblioteka funkcji matematycznych

def silnia_iteracyjna(n):
    # Oblicza silnię liczby n metodą iteracyjną (pętla)
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik

def silnia_rekurencyjna(n):
    # Oblicza silnię liczby n metodą rekurencyjną (funkcja woła samą siebie).
    if n <= 1:
        return 1
    return n * silnia_rekurencyjna(n - 1)

def nwd(a, b):
    # Oblicza Największy Wspólny Dzielnik algorytmem Euklidesa.
    while b:
        a, b = b, a % b
    return a

def czy_pierwsza(n):
    # Sprawdza, czy liczba n jest liczbą pierwszą.
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n):
    # Generuje listę n pierwszych wyrazów ciągu Fibonacciego.
    if n <= 0:
        return []
    if n == 1:
        return [0]
    ciag = [0, 1]
    while len(ciag) < n:
        ciag.append(ciag[-1] + ciag[-2])
    return ciag

# Sekcja testowa
if __name__ == "__main__":
    test_n = 5
    print(f"Silnia ({test_n}): {silnia_iteracyjna(test_n)}")
    print(f"NWD (48, 18): {nwd(48, 18)}")
    print(f"Czy {test_n} jest liczbą pierwszą? {czy_pierwsza(test_n)}")
    print(f"Fibonacci ({test_n}): {fibonacci(test_n)}")