import requests
from mymath.arithmetic import silnia, nwd
from mymath.sequences import fibonacci

def main():
    print("--- Test pakietu mymath ---")
    print(f"Silnia z 5: {silnia(5)}")
    print(f"NWD(48, 18): {nwd(48, 18)}")
    print(f"Fibonacci(10): {fibonacci(10)}")

    print("\n--- Test biblioteki zewnętrznej ---")
    try:
        r = requests.get("https://api.github.com")
        print(f"Status GitHub API: {r.status_code}")
    except:
        print("Brak połączenia z internetem.")

if __name__ == "__main__":
    main()