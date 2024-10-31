def pierwszy(n):
    a = 0
    for i in range(n):
        a += (-1) ** i * (3 * i - 1)
    return -a

def drugi(n):
    b = 1
    for i in range(n):
        b *= (-1) ** i * (4 * (i + 1))
    return b


def silnia(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * silnia(num - 1)

def trzeci(n):
    c = 0
    for i in range(1, n + 1):
        c += silnia(i)
    return c

def czwarty(n):
    gora = sum(range(1, n + 1))
    dol = 1
    for i in range(n):
        dol *= 2 + 4 * i
    return gora/dol

print(pierwszy(4))
print(drugi(3))
print(trzeci(3))
print(czwarty(4))