'''
Napisz program realizujący operacje na liście dwuwymiarowej
a)	Wypisanie elementów listy z podziałem na wiersze
b)	Zamiana dwóch kolumn listy numer1 i numer 2
c)	Zamiana dwóch wierszy listy wskazanych przez użytkownika

lista = [2, 3, 4, 7], [7, 6, 4, 2], [8, 9, 4, 1]
'''

lista = [[2, 3, 4, 7], [7, 6, 4, 2], [8, 9, 4, 1]]

#bierze index z listy i po kolei printuje go 
def printLista(lista):
    for row in lista:
        print(row)


#w każdej liście w liście bierze index a i oraz index b i zamienia go zrazem sobą
def zad_b(lista, num1, num2):
    for row in lista:
        row[num1], row[num2] = row[num2], row[num1]
    printLista(lista)
    
#zamienia dwa wiersze w liście na podstawie indeksów rowA i rowB
def zad_c(lista, rowA, rowB):
    lista[rowA], lista[rowB] = lista[rowB], lista[rowA]
    printLista(lista)
    
print(f"Zadanie a:")
printLista(lista.copy())

print("Zadanie b:")
zad_b(lista.copy(), 1, 3)

print("Zadanie c:")
zad_c(lista.copy(), 0, 2)
