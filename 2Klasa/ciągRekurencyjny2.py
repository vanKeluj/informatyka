def zad_f(n):
    if n == 1:
        return 1.5
    elif n==2:
        return 1
    return zad_f(n-2)+zad_f(n-1)-2

print(zad_f(6))

def zad_g(n):
    if n == 1:
        return -3
    elif n==2:
        return 1
    return zad_g(n-2)*zad_g(n-1)-1

print(zad_g(4))

def zad_h(n):
    if n == 1:
        return -2
    elif n==2:
        return 2.5
    elif n==3:
        return 3
    return zad_h(n-3)-zad_h(n-1)

print(zad_h(6))

def zad_i(n):
    if n == 1:
        return -1
    elif n==2:
        return 0
    elif n==3:
        return 0.5
    return zad_i(n-1)-zad_i(n-3)

print(zad_i(4))

def zad_j(n):
    if n == 1:
        return 0
    elif n==2:
        return 1
    elif n==3:
        return -1
    return zad_j(n-3)+zad_j(n-2)-zad_j(n-1)

print(zad_j(6))