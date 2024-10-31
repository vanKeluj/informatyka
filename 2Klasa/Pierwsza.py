def jest_Pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Podaj liczbe: "))

if jest_Pierwsza(n):
    print(f"{n} jest liczbą pierwszą")
else:
    print(f"{n} nie jest liczbą pierwszą")