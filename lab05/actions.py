import logging

def dodaj_wydatek(wydatki):
    try:
        kategoria = input("Kategoria: ").strip()
        if not kategoria:
            raise ValueError("Kategoria nie może być pusta!")
        kwota = float(input("Kwota: "))
        if kwota <= 0:
            raise ValueError("Kwota nie może być ujemna!")
        
        opis = input("Opis: ").strip()

        wydatki.append({
            "kategoria": kategoria,
            "kwota": kwota,
            "opis": opis
        })
    except ValueError as e:
        logging.error(f"Nieprawidłowe dane: {e}")

def oblicz_sumę(wydatki):
    stats = {}

    for w in wydatki:
        k = w['kategoria']
        stats[k] = stats.get(k, 0) + w['kwota']
     
    print("Statystyki")
    for k, suma in stats.items():
        print(f"{k}: {suma:.2f} PLN")