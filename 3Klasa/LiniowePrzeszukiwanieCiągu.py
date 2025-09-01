lista = [7, 5, 6, 5, 3, 4, 8, 2, 3]

def szukaj(L: list, n):
    if any(L[i] == n for i in range(len(L))):
        return ""
    else:
        return "nie "

def szukajdzielna(L: list, n):
    if any(L[i]%n==0 for i in range(len(L))):
        return ""
    else:
        return "nie "

def szukajwieksze(L: list, n):
    if all(L[i]>n for i in range(len(L))):
        return ""
    else:
        return "nie "


print(f"szukana liczba {szukaj(lista, 8)}znajduje się na liście")
print(f"szukana liczba {szukaj(lista, 7)}znajduje się na liście")
print(f"liczba podzielna przez 7 {szukajdzielna([7, 5, 6, 4, 5, 3, 4, 8, 2, 3], 7)}znajduje się na liście")
print(f"liczba podzielna przez 7 {szukajdzielna([9, 5, 6, 5, 3, 4, 8, 2, 3], 7)}znajduje się na liście")
print(f"liczby w liście {szukajwieksze([7, 9, 6, 8, 7, 7, 11, 9, 8, 8], 5)}są większe od 5")
print(f"liczby w liście {szukajwieksze([7, 9, 6, 8, 7, 7, 4, 11, 9, 8 ,1], 5)}są większe od 5")
