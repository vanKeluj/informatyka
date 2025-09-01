def selection_sort(T):
    n = len(T)
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if T[j] < T[k]:
                k = j
        
        T[i], T[k] = T[k], T[i]
    
    return T 

T = [1, 8, 6, 0, 5, 4, 3, 7]
print("Przed sortowaniem:", T)
posortowana = selection_sort(T)
print("Po sortowaniu:", posortowana)
