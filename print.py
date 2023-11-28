def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)

def sum_of_factorials(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += factorial(i)
    return total_sum

print(sum_of_factorials(3))
