def decimal_to_octal(decimal_num):
    octal_num = []
    while decimal_num > 0:
        remainder = decimal_num % 8
        octal_num.insert(0, remainder)
        decimal_num //= 8
    return octal_num

def octal_to_decimal(octal_num):
    decimal_num = []
    power = 0
    while octal_num > 0:
        remainder = octal_num % 10
        decimal_num.insert(0, remainder * (8 ** power))
        power += 1
        octal_num //= 10
    return sum(decimal_num)

# Example usage:
into_octal_number = int(input("Give decimal Number: "))
print("Decimal:", into_octal_number, "=> Octal:", decimal_to_octal(into_octal_number))

into_decimal_number = int(input("Give octal Number: "))
print("Octal:", into_octal_number, "=> Decimal:", octal_to_decimal(into_decimal_number))
