def bubble_sort(T):
    n = len(T)
    for i in range(n):
        for j in range(0, n-1-i):
            if T[j] > T[j+1]:
                T[j], T[j+1] = T[j+1], T[j]
    return T

# Przykładowe wywołanie
T = [9, 8, 7, 0, 5, 4, 3, 2]
print("Przed sortowaniem:", T)
posortowana = bubble_sort(T)
print("Po sortowaniu:", posortowana)