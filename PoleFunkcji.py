import math

def Pole(p,q,n,x):
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

print(Pole(3, 5, 20, 1))
print(Pole(2, 4, 20, 2))
print(Pole(1, 4, 20, 3))
print(Pole(1, 4, 20, 4))
