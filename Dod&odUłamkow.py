def NWW(a,b) :
    return a*b/NWD(a, b)

def NWD (a,b):
    while b>0:
        r = a%b
        a=b
        b=r
    return a

l1 = int(input("Podaj pierwszy licznik: "))
m1 = int(input("Podaj pierwszy minanownik: "))
l2 = int(input("Podaj drugi licznik: "))
m2 = int(input("Podaj drugi minanownik: "))

def dod(a, b, c, d):
    return (a*d + c*b) / (b*d)

def NWWdod(a, b, c, d):
    nww = NWW(b, d)
    return (a * (nww / b) + c * (nww / d)) / nww

def mnoz(a, b, c, d):
    nwd1 = NWD(a, d)
    nwd2 = NWD(b, c)
    return ((a / nwd1) * (c / nwd2)) / ((b / nwd2) * (d / nwd1))


print(dod(l1, m1, l2, m2))
print(NWWdod(l1, m1, l2, m2))
print(mnoz(l1, m1, l2, m2))