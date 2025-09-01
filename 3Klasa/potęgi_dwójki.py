def pot(num:int):
    x = num
    list = []
    temp = 0
    while x > 0:
        if is_power_of_two(x) == True:
            list.append(x)
            x = temp
            temp = 0
        else:
            x -= 1
            temp += 1
    
    return len(list)

def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

print(pot(18))