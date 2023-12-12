#Pierwszy sposób
def silnian(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnian(n - 1)
    
def silniak(k):
    if k == 0 or k == 1:
        return 1
    else:
        return k * silniak(k - 1)

def silniank(n,k):
    if n-k == 0 or n-k == 1:
        return 1
    else:
        return n-k * silniak(n-k - 1)


print(silnian(6)/(silniak(4)*silniank(6,4)))

#drógi sposób
def silnia(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * silnian(x - 1)

def SymbolNewtona(n,k):
    if k>=0 and n>=k:
        return silnia(n)/(silnia(k)*silnia(n-k))
    else:
        return "nie można tego zrobić"

print(SymbolNewtona(6,4))
print(SymbolNewtona(5,6))