import math

def F(num,x):
    if num == 1:
        return x**2 - x - 3
    elif num == 2:
        return -(x**3) - (x**2) + 1
    elif num == 3:
        return math.cos(x) + 1
    elif num == 4:
        return 2*x/x**2 + 5       


def PoleTrapez(p,q,n,x):
    dl = (q-p)/n
    s = 0
    for i in range(n):
        s += math.fabs(F(x, p+i*dl))
    P = dl/2*(math.fabs(F(x, p)) + math.fabs(F(x, q)) + 2*s)
    
    return P


def PoleKwadrat(p,q,n,x):
    P = 0
    dl =  (q-p)/n
    for i in range(1,n+1):
        h = abs(F(x, p+dl*i-dl/2))
        P += h*dl
        
    return P


print("Metoda kwadrat: ", PoleKwadrat(3, 5, 20, 1))
print("Metoda kwadrat: ", PoleKwadrat(2, 4, 20, 2))
print("Metoda kwadrat: ", PoleKwadrat(1, 4, 20, 3))
print("Metoda kwadrat: ", PoleKwadrat(1, 4, 20, 4))


print("Metoda Trapez: ", PoleTrapez(3, 5, 20, 1))
print("Metoda Trapez: ", PoleTrapez(2, 4, 20, 2))
print("Metoda Trapez: ", PoleTrapez(1, 4, 20, 3))
print("Metoda Trapez: ", PoleTrapez(1, 4, 20, 4))