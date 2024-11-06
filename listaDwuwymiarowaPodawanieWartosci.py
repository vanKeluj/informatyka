'''
1	3	5
6	8	10
11	13	15
16	18	20
'''
def generate_list():
    lista = []
    
    for start in range(1, 17, 5): 
        lista.append([start, start+2, start+4]) 
    
    return lista

lista = generate_list()
def zad_a(lista, numWiersz, numKolumn):
    print ("Lista: ")
    for row in lista:
        print(row)
    print(f"Elemnet listy w kolunnie {numKolumn+1} i w wierszu {numWiersz+1} to {lista[numWiersz][numKolumn]}") 

kolumna = int(input("Podaj index kolumny: ")) - 1
wiersz = int(input("Podaj index wiersza: ")) - 1
zad_a(lista, wiersz, kolumna)