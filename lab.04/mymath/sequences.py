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