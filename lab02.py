def analiza_ocen():
    # 1. Pobranie danych od użytkownika
    wejscie = input("Podaj oceny rozdzielone spacją (np. 3 4.5 5 2): ")
    oceny = [float(x) for x in wejscie.split()]

    if not oceny:
        print("Lista ocen jest pusta!")
        return

    # 2. Obliczenie średniej arytmetycznej
    suma = sum(oceny)
    srednia = suma / len(oceny)

    # 3. Wyznaczenie wartości minimalnej i maksymalnej
    min_val = oceny[0]
    max_val = oceny[0]
    for o in oceny:
        if o < min_val:
            min_val = o
        if o > max_val:
            max_val = o

    # 4. Obliczenie mediany 
    posortowane = sorted(oceny)
    n = len(posortowane)
    srodek = n // 2

    if n % 2 != 0:
        mediana = posortowane[srodek]
    else:
        mediana = (posortowane[srodek - 1] + posortowane[srodek]) / 2

    # 5. Bonus: List comprehension
    powyzej_sredniej = [o for o in oceny if o > srednia]

    # 6. Zapisanie wyników do słownika
    wyniki = {
        "srednia": round(srednia, 2),
        "mediana": mediana,
        "minimum": min_val,
        "maksimum": max_val,
        "ilosc powyzej sredniej": len(powyzej_sredniej)
    }

    # 7. WYDRUK 
    print("\n--- RAPORT ---")
    for klucz, wartosc in wyniki.items():
        print(f"{klucz.capitalize()}: {wartosc}")

# Wywołanie funkcji
if __name__ == "__main__":
    analiza_ocen()