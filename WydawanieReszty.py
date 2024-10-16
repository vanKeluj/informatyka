def wydaj_reszte(reszta):
    T = [20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1] # Nominały w groszach
    K = [0] * 14 # Liczba nominałów wydanych
    x = 0 # Liczba nominałów wydanych
    i = 0 # Indeks dla tablicy T

    # na danym indeksie w tablicy K sprawdzamy czy jest podzielny przez ten sam indeks w tablicy T
    while reszta > 0:
        K[i] = reszta // T[i]
        reszta = reszta % T[i]
        i += 1
    
    # jeśli na indeksie i w tablicy K jest numer większy od 0 to podaje ile go jest i dodaje do sumy wydanych nominałów
    for i in range(14):
        if K[i] > 0:
            print(f"{T[i]/100:.2f} zł: {K[i]} szt.")
            x += K[i]
    
    print("Liczba nominałów wydanych", x)

    return K

# Przykładowe użycie
reszta = int(input("Podaj kwotę reszty w groszach: "))
print("Łączna liczba wydanych nominałów: ", wydaj_reszte(reszta))