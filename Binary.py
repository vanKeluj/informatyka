def decimal_to_binary(n):
    binary_return = []
    
    if n == 0:
        return [0]
    
    while n > 0:
        ones = n % 2
        binary_return.insert(0, ones)
        n = n // 2
    
    return binary_return


n= int(input("Podaj Liczbę: "))
print("Twoja liczba w binarnym to:", decimal_to_binary(n))