def insertion_sort(T):
    n = len(T)
    for i in range(1, n):
        temp = T[i]
        j = i - 1
        while j >= 0 and T[j] > temp:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = temp
    return T

# Przykładowe dane wejściowe
T = [3, 8, 2, 0, 5, 4, 1, 9]
print("Przed sortowaniem:", T)
posortowana = insertion_sort(T)
print("Po sortowaniu:", posortowana)
