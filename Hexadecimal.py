hexadecimal_Dict = {
    10 : "A",
    11 : "B",
    12 : "C",
    13 : "D",
    14 : "E",
    15 : "F"
}

rev_hexadecimal_Dict = {
    "A": 10,
    "B": 11,
    "C": 12,
    "D": 13,
    "E": 14,
    "F": 15
}


def decimal_to_hexadecimal(decimal_num):
    hexadecimal_num = []
    while decimal_num > 0:
        remainder = decimal_num % 16
        if remainder < 10:
            hexadecimal_num.insert(0, remainder)
        else:
            hexadecimal_num.insert(0, hexadecimal_Dict[remainder])
        decimal_num //= 16
    return hexadecimal_num

def hexadecimal_to_decimal(hexadecimal_num):
    decimal_num = 0
    power = 0
    for character in reversed(hexadecimal_num):
        if character.isdigit():
            decimal_num += int(character) * (16 ** power)
        else:
            decimal_num += (rev_hexadecimal_Dict[character] ) * (16 ** power)
        power += 1
    return decimal_num

# Example usage:
into_hexadecimal_number = int(input("Give decimal Number: "))
print("Decimal:", into_hexadecimal_number, "=> Hexadecimal:", decimal_to_hexadecimal(into_hexadecimal_number))

into_decimal_number = input("Give hexadecimal Number: ")
print("Hexadecimal:", into_decimal_number, "=> Decimal:", hexadecimal_to_decimal(into_decimal_number))
