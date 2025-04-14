import math   


def PoleKwadrat(p,q,n,f):
    P = 0
    dl =  (q-p)/n
    
    for i in range(1,n+1):
        h = abs(f(p+dl*i-dl/2))
        P += h*dl
        
    return P


def PoleTrapez(p,q,n,f):
    dl = (q-p)/n
    s = 0
    
    for i in range(n):
        s += math.fabs(f(p+i*dl))
    
    P = dl/2*(math.fabs(f(p)) + math.fabs(f(q)) + 2*s)
    
    return P


print("Metoda kwadrat: ", PoleKwadrat(3, 5, 20, lambda x: x**2 - x - 3))
print("Metoda kwadrat: ", PoleKwadrat(2, 4, 20, lambda x: -(x**3) - (x**2) + 1))
print("Metoda kwadrat: ", PoleKwadrat(1, 4, 20, lambda x: math.cos(x) + 1))
print("Metoda kwadrat: ", PoleKwadrat(1, 4, 20, lambda x: 2*x/x**2 + 5))

print("Metoda Trapez: ", PoleTrapez(3, 5, 20, lambda x: x**2 - x - 3))
print("Metoda Trapez: ", PoleTrapez(2, 4, 20, lambda x: -(x**3) - (x**2) + 1))
print("Metoda Trapez: ", PoleTrapez(1, 4, 20, lambda x: math.cos(x) + 1))
print("Metoda Trapez: ", PoleTrapez(1, 4, 20, lambda x: 2*x/x**2 + 5))