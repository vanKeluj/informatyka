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

print("a) Wypisanie wszystkich elementów listy:", lista)

liczba_elementow = sum(1 for i in range(len(lista)) if i % 5 != 0)
print("b) Liczba elementów, których indeks nie jest podzielny przez 5:", liczba_elementow)