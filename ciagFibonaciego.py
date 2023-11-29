#pisze tą liczbę w ciągu
def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))


#pisze ciąg
def fibonacci2(n):
    a = [1, 1]
    while len(a) < n:
        a.append(a[-1] + a[-2])
    return a[:n]


print(fibonacci2(10))