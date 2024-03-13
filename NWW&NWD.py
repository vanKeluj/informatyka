def nww(a,b) :
    return a*b/NWD(a, b)

def NWD (a,b):
    while b>0:
        r = a%b
        a=b
        b=r
    return a

def rekNWD(a,b):
    if  b==0:
        return a
    else:
        return rekNWD(b,a%b)

def odNWD(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def odrekNWD(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print(NWD(32,44))
print(rekNWD(32,44))
print(odNWD(32,44))
print(nww(32,44))

l = int(input("Podaj licznik: "))
m = int(input("Podaj minanownik: "))

def skrocenie(l,m):
    nwd = (NWD(l,m))
    l = l /nwd
    m = m / nwd
    return (l,m)

print(skrocenie(l,m))