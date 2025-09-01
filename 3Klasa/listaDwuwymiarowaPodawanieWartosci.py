'''
1	3	5
6	8	10
11	13	15
16	18	20
'''

def zad_a(numWiersz, numKolumn):
    lista = []
    for row in range(numWiersz):
        lista.append([(1+row*5)+(2*col) for col in range(numKolumn)])
    
    print ("Lista: ")
    for row in lista:
        print(row)

kolumna = int(input("Podaj ilość kolumn: "))
wiersz = int(input("Podaj ilość wierszy: "))
zad_a(wiersz, kolumna)