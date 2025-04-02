def Pierwiastek(p,E,L):
    a = p
    i = 0
    while abs(a - (p / a)) > E and i < L:
        a = (a + (p / a)) / 2
        i += 1
    return a

print(Pierwiastek(10, 0.00001, 50))
print(Pierwiastek(125, 0.001, 50))
print(Pierwiastek(1024, 0.001, 50))
print(Pierwiastek(2000, 0.001, 50))
