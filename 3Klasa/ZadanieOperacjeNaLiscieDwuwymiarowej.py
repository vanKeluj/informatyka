'''
Napisz program realizujący operacje na liście dwuwymiarowej
a)	 Wypisywanie elementów listy z podziałem na wiersze
b)	 Obliczenie iloczynu tych elementów, których wartość jest większa od 5
c)	 Obliczenie liczby tych elementów listy, których wartość jest różna od 0
d)	 Sprawdzenie, czy na liście znajduje się element, którego wartość jest nie mniejsza od 20
Lista = [2, 3, 0, 5], [7, 6, 1, 0], [2, 9, 0, 5]
'''
lista = [2, 3, 0, 5], [7, 6, 1, 0], [2, 9, 0, 5]

#zadanie a
def zad_a(Lista):
    for i in range(len(Lista)):
        print(Lista[i])

zad_a(lista)


#zadanie b
def zad_b(lista):
    iloczyn = 1
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] > 5:
                iloczyn *= lista[i][j]
    return iloczyn

print(f"iloczyn elementów, których wartość jest większa od 5: {zad_b(lista)}")


#zadanie c
def zad_c(lista):
    elementy_listy_ruzne_od_zero = 0
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if lista[i][j] != 0:
                elementy_listy_ruzne_od_zero += 1
    return elementy_listy_ruzne_od_zero

print(f"Liczba elementów listy, których wartość jest różna od zera: {zad_c(lista)}")


#zadanie d
print(f"Czy na liście znajduje się element, których wartość jest nie mniejsza od 20: {any(kolumna > 20 for wiersz in lista for kolumna in wiersz )}")