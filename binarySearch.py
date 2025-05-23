def szukaj(arr, low, high, x):
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return szukaj(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return szukaj(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1

# Przykładowe wywołanie
T = [-8, -7, -6, -2, 0, 2, 3, 4, 5, 7, 8, 10, 12, 13, 17, 19]
szukana = 15
wynik = szukaj(T, 0, len(T) - 1, szukana)


print(wynik)