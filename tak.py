x = 4
y = 6
z = 2

def zad_a(x,y,z):
    if x%2==0 or y%2==0 or z%2==0:
        print("Tak")
    else:
        print("Nie")

def zad_b(x,y,z):
    if x%2==0:
        print("Nie")
    elif y%2==0:
        print("Nie")
    elif z%2==0:
        print("Nie")
    else:
        print("Tak")


zad_a(4,6,2)
zad_b(4,5,2)