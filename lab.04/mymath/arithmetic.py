def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

def silnia(n):
    if n == 0:
        return 1
    wynik = 1
    for i in range(1, n + 1):
        wynik *= i
    return wynik