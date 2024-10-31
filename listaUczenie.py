'''
Oblicz sumę wszytskich elementów listy
Oblicz iloczyn wszystkich elementów listy które są mniejse od 6
oblicz liczbę tych elementów listy, których indeks nie jest podzielny przez 5
wyzeruj te elementy listy, które mają nieparzysty indeks zawarty w predziale [3,8] i  wyświetlanie tej listy
'''
lista = [3,4,5,5,7,9,4,2,1]

# 1. Oblicz sumę wszytskich elementów listy
suma = sum(lista)
print("Suma wszystkich elementów listy:",suma)

# 2. Oblicz iloczyn wszystkich elementów listy które są mniejse od 6
iloczyn = 1
for element in lista:
    if element < 6:
        iloczyn *= element
print("Iloczyn elementów mniejszych od 6:",iloczyn)

# 3. Oblicz liczbę tych elementów listy, których indeks nie jest podzielny przez 5
liczba_elementow = 0
for i in range(len(lista)):
    if i % 5 != 0:
        liczba_elementow += 1
print("Liczba elementów, których indeks nie jest podzielny przez 5:",liczba_elementow)

# 4. Wyzeruj te elementy listy, które mają nieparzysty indeks zawarty w predziale [3,8] i wyświetl tę listę
for i in range(3, 8,):
    if i % 2 != 0:
        lista[i] = 0
print("Lista po wyzerowaniu elementów o nieparzystych indeksach w przedziale [3,8]:",lista)
