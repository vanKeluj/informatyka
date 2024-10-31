'''
Sprawdzenie czy na liscie znajduje się element o wartości różnej od 2
sprawdzenie czy na liscie wartości wszystkich elementów są nieujemne
sprawdzenie czy na liscie znajduje się element, którego wartość nie zawiera się w przedziale [5,8]
sprawdzenie czy na liscie wszystkie elementy mają wartość wiekszą od 11 
sprawdzenie czy na liscie jest element o wartości podanej przez urzytkownika 
'''
lista = [3,4,5,5,7,9,4,2,1]
krotka = (3,4,5,5,7,9,4,2,1)

# 1. Sprawdzenie czy na liscie znajduje się element o wartości różnej od 2
czy_rozne_od_2 = any(x != 2 for x in lista)
print("1. Czy na liście znajduje się element o wartości różnej od 2?", czy_rozne_od_2)

# 2. Sprawdzenie czy na liscie wartości wszystkich elementów są nieujemne
czy_wszystkie_nieujemne = all(x >= 0 for x in lista)
print("2. Czy wszystkie elementy listy są nieujemne?", czy_wszystkie_nieujemne)

# 3. Sprawdzenie czy na liscie znajduje się element, którego wartość nie zawiera się w przedziale [5,8]
czy_poza_przedzialem = any(x < 5 or x > 8 for x in lista)
print("3. Czy na liście jest element spoza przedziału [5,8]?", czy_poza_przedzialem)

# 4. Sprawdzenie czy na liscie wszystkie elementy mają wartość większą od 11
czy_wszystkie_wieksze_od_11 = all(x > 11 for x in lista)
print("4. Czy wszystkie elementy listy są większe od 11?", czy_wszystkie_wieksze_od_11)

# 5. Sprawdzenie czy na liscie jest element o wartości podanej przez użytkownika
wartosc_uzytkownika = int(input("Podaj wartość do sprawdzenia: "))
czy_jest_wartosc_uzytkownika = wartosc_uzytkownika in lista
print("5. Czy na liście jest element o wartości", wartosc_uzytkownika, "?", czy_jest_wartosc_uzytkownika)