def NWW(a,b) :
    return a*b/NWD(a, b)

def NWD (a,b):
    while b>0:
        r = a%b
        a=b
        b=r
    return a

def skrocenie(a,b):
    nwd = (NWD(a,b))
    a = a /nwd
    b = b / nwd
    u = [a,b]
    return u

l1 = int(input("Podaj pierwszy licznik: "))
m1 = int(input("Podaj pierwszy minanownik: "))
l2 = int(input("Podaj drugi licznik: "))
m2 = int(input("Podaj drugi minanownik: "))

def dod(a, b, c, d):
    e = (a*d + c*b)
    f= (b*d)
    return skrocenie(e,f)

def NWWdod(a, b, c, d):
    nww = NWW(b, d)
    e = (a * (nww / b) + c * (nww / d))
    f = nww
    return skrocenie(e,f)

def mnoz(a, b, c, d):
    nwd1 = NWD(a, d)
    nwd2 = NWD(b, c)
    e = ((a / nwd1) * (c / nwd2))
    f = ((b / nwd2) * (d / nwd1))
    return skrocenie(e,f)

def dziel(a, b, d, c):
    nwd1 = NWD(a, d)
    nwd2 = NWD(b, c)
    e = ((a / nwd1) * (c / nwd2))
    f = ((b / nwd2) * (d / nwd1))
    return skrocenie(e,f)

def od(a, b, c, d):
    e = (a*d - c*b)
    f= (b*d)
    return skrocenie(e,f)


print("Dodawanie: ", dod(l1, m1, l2, m2))
print("Dodawanie: ", NWWdod(l1, m1, l2, m2))
print("Mnożene: ", mnoz(l1, m1, l2, m2))
print("Dzielenie: ", dziel(l1, m1, l2, m2))
print("Odejmowanie: ", od(l1, m1, l2, m2))