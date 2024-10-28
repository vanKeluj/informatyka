'''
Zadanie
Napisz program wykonujący operacje na liście jednowymiarowej:
a)	Wypisanie wszystkich elementów listy;
b)	 Obliczenie liczby tych elementów listy, których indeks nie jest podzielny przez 5;
c)	Zwiększenie o 2 tych elementów listy, które mają nieparzysty indeks zawarty w przedziale [3,8] i wypisanie tej liczby;
d)	 Sprawdzenie czy na wczytanej liście wartości wszystkich elementów są nieujemne;
e)	 Obliczenie iloczynu tych elementów listy, których wartość jest równa 5;
f)	Sprawdzenie czy na wczytanej liście znajduje się element, którego wartość nie zawiera się w przedziale [5,8]
'''
lista  =  [9, 4, 3, 5, 7, 9, 4, 2, 1, 5]


#region Zadania
# a) Wypisanie wszystkich elementów listy


# b) Obliczenie liczby tych elementów listy, których indeks nie jest podzielny przez 5
def zad_b():
    b = lista.copy()
    liczba_elementow = 0
    for i in range(len(b)):
        if i % 5 != 0:
            liczba_elementow += 1
    return liczba_elementow


# c) Zwiększenie o 2 tych elementów listy, które mają nieparzysty indeks zawarty w przedziale [3,8] i wypisanie tej liczby
def zad_c():
    c = lista.copy()
    liczba_zmienionych = 0
    for i in range(3, 8):
        if i % 2 != 0:
            c[i] += 2
            liczba_zmienionych += 1
    return liczba_zmienionych, c


# d) Sprawdzenie czy na wczytanej liście wartości wszystkich elementów są nieujemne
czy_wszystkie_nieujemne = any (x for x in lista if x > 0)


# e) Obliczenie iloczynu tych elementów listy, których wartość jest równa 5
def zad_e():
    e = lista.copy()
    iloczyn = 1
    for x in lista:
        if x == 5:
            iloczyn *= x
    return iloczyn


# f) Sprawdzenie czy na wczytanej liście znajduje się element, którego wartość nie zawiera się w przedziale [5,8]
Znajduje_sie_w_przedziale  = any([x for x in lista if x < 5 or x > 8])
#endregion



print("a) Wypisanie wszystkich elementów listy:", lista)
print("b) Liczba elementów, których indeks nie jest podzielny przez 5:",zad_b())
print("c) Liczba zmienionych elementów:", zad_c())
print("d) Czy wszystkie elementy listy są nieujemne?", czy_wszystkie_nieujemne)
print("e) Iloczyn elementów o wartości 5:", zad_e())
print("f) Czy na liście znajduje się element, którego wartość nie zawiera się w przedziale [5,8]?", Znajduje_sie_w_przedziale)