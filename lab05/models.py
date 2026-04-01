import json
import logging
from pathlib import Path

# Konfiguracja logowania
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Scieżka do pliku z danymi
DATA_FILE = Path("wydatki.json")

# Finkcja wzytuje dane z pliku lub tworzy nową listę, jeśli plik nie istnieje
def inicjalizuj_dane():
    if not DATA_FILE.exists():
        logging.warning("Plik nie istnieje.Tworzenie nowej bazy danych")
        return []
    try: 
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
                  return json.load(f)
    except json.JSONDecodeError:
            logging.error("Błąd formatu pliku JSON. Zaczynamy z pustą listą")
            return []
        

def zapisz_dane(wydatki):
    try: 
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(wydatki, f, indent=4, ensure_ascii=False)
        logging.info("Dane zostały zapisane.")
    except Exception as e:
             logging.error(f"Wystąpił nieoczekiwany błąd: {e}")
             return []

 




