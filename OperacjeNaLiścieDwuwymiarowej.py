"""
Napisz kod programu wykonującego następujące operacje na liście dwuwymiarowej
a)	Wypisywanie elementów listy z podziałem na wiersze
b)	Obliczenie sumy tych elementów, które są niepodzielne przez 3
c)	Zmniejszenie o 3 tych elementów listy, które nie znajdują się na głównej przekątnej i wypisanie tej listy

lista = [2, 3, 4, 5], [7, 6, 4, 5], [8, 9, 4, 5]
"""
lista = [[2, 3, 4, 5], [7, 6, 4, 5], [8, 9, 4, 5]]
def zad_a(T,m):
    for i in range(m):
        print(T[i])

def zad_b(T,m,n):
    suma = 0
    for i in range(m):
        for j in range(n):
            if T[i][j] % 3 != 0:
                suma += T[i][j]
    return suma

def zad_c(T,m,n):
    for i in range(m):
        for j in range(n):
            if i != j:
                T[i][j] -= 3
        print(T[i])

zad_a(lista, 3)
print(f"suma = {zad_b(lista,3,4)}")
zad_c(lista,3,4)