import re
'''
Napisz program wykonujący działania na napisach
a)	 Obliczenie liczby znaków d
b)	 Wypisanie znaków w odwrotnej kolejności (od ostatniego znaku do pierwszego)
c)	 Obliczenie liczby znaków różnych od a
d)	 Zamiana znaków różnych od b i B na a
e)	 Wypisanie tylko tych znaków, które są różne od s
f)	Obliczenie liczby znaków różnych od d , które mają indeks podzielny przez 3
g)	 Zamiana znaków m na R

'''
tekst = "subdominanta"

# a) Obliczenie liczby znaków 'd'
print(tekst.count('d'))


# b) Wypisanie znaków w odwrotnej kolejności
print(tekst[::-1])


# c) Obliczenie liczby znaków różnych od 'a'
print(len(tekst.replace('a','')))


# d) Zamiana znaków różnych od 'b' i 'B' na 'a'
print(re.sub('[^bB]','a',tekst))


# e) Wypisanie tylko tych znaków, które są różne od 's'
print(tekst.replace('s',''))


# f) Obliczenie liczby znaków różnych od 'd', które mają indeks podzielny przez 3
print(len(tekst[::3].replace('d','')))
def f():
    diff_d_count = 0
    for char in range((len(tekst))-1):
        if char % 3 == 0 and tekst[char] != 'd':
            diff_d_count += 1
    return diff_d_count
print(f())

# g) Zamiana znaków 'm' na 'R'
print(tekst.replace('m', 'R'))

