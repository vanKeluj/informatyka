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
# a) Wypisanie wszystkich elementów listy
print("a) Wypisanie wszystkich elementów listy:", lista)


# b) Obliczenie liczby tych elementów listy, których indeks nie jest podzielny przez 5
liczba_elementow = 0
for i in range(len(lista)):
    if i % 5 != 0:
        liczba_elementow += 1
print("b) Liczba elementów, których indeks nie jest podzielny przez 5:",liczba_elementow)


# c) Zwiększenie o 2 tych elementów listy, które mają nieparzysty indeks zawarty w przedziale [3,8] i wypisanie tej liczby
liczba_zmienionych = 0
for i in range(3, 8):
    if i % 2 != 0:
        lista[i] += 2
        liczba_zmienionych += 1
print("c) Liczba zmienionych elementów:", liczba_zmienionych)
print("   Lista po zmianie:", lista)

lista  =  [9, 4, 3, 5, 7, 9, 4, 2, 1, 5]
# d) Sprawdzenie czy na wczytanej liście wartości wszystkich elementów są nieujemne
czy_wszystkie_nieujemne = any (x for x in lista if x > 0)
print("d) Czy wszystkie elementy listy są nieujemne?", czy_wszystkie_nieujemne)


# e) Obliczenie iloczynu tych elementów listy, których wartość jest równa 5
iloczyn = 1
for x in lista:
    if x == 5:
        iloczyn *= x
print("e) Iloczyn elementów o wartości 5:", iloczyn)


# f) Sprawdzenie czy na wczytanej liście znajduje się element, którego wartość nie zawiera się w przedziale [5,8]
Znajduje_sie_w_przedziale  = any([x for x in lista if x < 5 or x > 8])
print("f) Czy na liście znajduje się element, którego wartość nie zawiera się w przedziale [5,8]?", Znajduje_sie_w_przedziale)