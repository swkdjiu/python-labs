import sys
import datetime

my_name = 'Yana'
now = datetime.datetime.now()

print(f"Cześć! Mam na imię {my_name}.")
print(f"Dzisiejsza data: {now.strftime('%d.%m.%Y')}")
print(f"Wersja Python: {sys.version}") 
     