lista = [7, 5, 6, 5, 3, 4, 8, 2, 3]

def szukaj(L: list, n):
    if any(L[i] == n for i in range(len(L))):
        return ""
    else:
        return "nie "


print(f"szukana liczba {szukaj(lista, 300)}znajduje się na liście")
print(f"szukana liczba {szukaj(lista, 7)}znajduje się na liście")