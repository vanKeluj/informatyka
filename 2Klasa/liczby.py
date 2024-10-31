def pierwszy(n):
    #dol = sum(range(1, n + 1))
    a = (2 * n) / sum(range(1, n + 1))
    return a

def drugi(n):
    b = sum(1 / (2 * i) for i in range(1, n + 1))
    return b

def trzeci(n):
    c = 1
    for i in range(1, n + 1):
        x = (i + 3) / n
        c *= x
    return c

def czwarty(n):
    d = sum((2 * 3 * (2 ** i)) / (i + 1) for i in range(0,n))
    return d

print(pierwszy(4))
print(drugi(3))
print(trzeci(3))
print(czwarty(4))