def plecak_dynamiczny(n, waga, W, C):
    # Inicjalizacja tablic Wartości i Numery
    Wartosci = [[0 for _ in range(waga + 1)] for _ in range(n + 1)]
    Numery = [[0 for _ in range(waga + 1)] for _ in range(n + 1)]
    
    # Krok 2: Dla kolejnych wartości i: 1,2, …, n, wykonuj krok 3.
    for i in range(1, n + 1):
        # Krok 3: Dla kolejnych wartości j: 1,2, …, waga, wykonuj krok 4.
        for j in range(1, waga + 1):
            # Krok 4: Aktualizacja tablic Wartości i Numery
            if j >= C[i-1]:
                if Wartosci[i-1][j] < Wartosci[i][j - C[i-1]] + W[i-1]:
                    Wartosci[i][j] = Wartosci[i][j - C[i-1]] + W[i-1]
                    Numery[i][j] = i
                else:
                    Wartosci[i][j] = Wartosci[i-1][j]
                    Numery[i][j] = Numery[i-1][j]
            else:
                Wartosci[i][j] = Wartosci[i-1][j]
                Numery[i][j] = Numery[i-1][j]

    # Krok 5: Wypisanie maksymalnej wartości zapakowanego plecaka
    max_wartosc = Wartosci[n][waga]
    print("Maksymalna wartość zapakowanego plecaka:", max_wartosc)

    # Odczyt przedmiotów umieszczonych w plecaku
    przedmioty_w_plecaku = []
    j = waga
    for i in range(n, 0, -1):
        if Numery[i][j] != 0:
            przedmiot = Numery[i][j]
            przedmioty_w_plecaku.append(przedmiot)
            j -= C[przedmiot - 1]
    
    print("Numery przedmiotów umieszczonych w plecaku:", przedmioty_w_plecaku)

# Przykład danych wejściowych
n = 5  # liczba przedmiotów
waga = 11  # maksymalna pojemność plecaka
W = [8,3,1,2,1] # wartości przedmiotów
C = [4,2,1,3,7]   # wagi przedmiotów

# Uruchomienie algorytmu
plecak_dynamiczny(n, waga, W, C)
