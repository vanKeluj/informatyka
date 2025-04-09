import math

def PoleTrapez(p,q,n,x):
    dl =  (q-p)/n
    s = 0
    for i in range(n):
        if x == 1:
            s += math.fabs(f1(p+i*dl))
        elif x == 2:
            s += math.fabs(f2(p+i*dl))
        elif x == 3:
            s += math.fabs(f3(p+i*dl))
        elif x == 4:
            s += math.fabs(f4(p+i*dl))
    if x == 1:
        P = dl/2*(math.fabs(f1(p)) + math.fabs(f1(q)) + 2*s)
    elif x == 2:
        P = dl/2*(math.fabs(f2(p)) + math.fabs(f2(q)) + 2*s)
    elif x == 3:
        P = dl/2*(math.fabs(f3(p)) + math.fabs(f3(q)) + 2*s)
    elif x == 4:
        P = dl/2*(math.fabs(f4(p)) + math.fabs(f4(q)) + 2*s)
    return P


def PoleKwadrat(p,q,n,x):
    P = 0
    dl =  (q-p)/n
    for i in range(1,n+1):
        if x == 1:
            h = abs(f1(p+dl*i-dl/2))
        elif x == 2:
            h = abs(f2(p+dl*i-dl/2))
        elif x == 3:
            h = abs(f3(p+dl*i-dl/2))
        elif x == 4:
            h = abs(f4(p+dl*i-dl/2))
        P += h*dl
    return P
      
def f1(x):
    return x**2 - x - 3

def f2(x):
    return -(x**3) - (x**2) + 1

def f3(x):
    return math.cos(x) + 1

def f4(x):
    return 2*x/x**2 + 5

print("Metoda kwadrat: ", PoleKwadrat(3, 5, 20, 1))
print("Metoda kwadrat: ", PoleKwadrat(2, 4, 20, 2))
print("Metoda kwadrat: ", PoleKwadrat(1, 4, 20, 3))
print("Metoda kwadrat: ", PoleKwadrat(1, 4, 20, 4))

print("Metoda Trapez: ", PoleTrapez(3, 5, 20, 1))
print("Metoda Trapez: ", PoleTrapez(2, 4, 20, 2))
print("Metoda Trapez: ", PoleTrapez(1, 4, 20, 3))
print("Metoda Trapez: ", PoleTrapez(1, 4, 20, 4))