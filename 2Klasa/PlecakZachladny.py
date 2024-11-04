def Plecak(W,C,n):
    wynik = 0
    dlugosc = len(W)
    K = [0]*dlugosc
    print(K)
    for i in range(dlugosc):
        K[i] = n // C[i]
        n -= K[i] * C[i]
        wynik += K[i] * W[i]
    return wynik, K

print(Plecak([8,3,1,2,1],[4,2,1,3,7],11))