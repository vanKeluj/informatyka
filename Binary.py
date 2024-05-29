def decimal_to_binary(n):
    binary_return = []
    
    if n == 0:
        return [0]
    
    while n > 0:
        reminder = n % 2
        binary_return.insert(0, reminder)
        n = n // 2
    
    return binary_return

def binary_to_decimal(n):
    decimal = 0
    power = 1
    while n>0:
        rem = n%10
        n = n//10
        decimal += rem*power
        power = power*2
        
    return decimal


x = int(input("Enter a binary number: "))
print("Decimal representation:", binary_to_decimal(x))

n= int(input("Podaj Liczbę: "))
print("Twoja liczba w binarnym to:", decimal_to_binary(n))