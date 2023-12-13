def sequence_a(n):
    if n == 1:
        return 4
    else:
        return sequence_a(n - 1) + 3

print(sequence_a(6))

def sequence_b(n):
    if n == 1:
        return 2
    else:
        return sequence_b(n - 1) * 2

print(sequence_b(5))

def sequence_c(n):
    if n == 1:
        return 2
    else:
        return sequence_c(n - 1) * -3

print(sequence_c(6))

def sequence_d(n):
    if n == 1:
        return -10
    else:
        return sequence_d(n - 1) / -2

print(sequence_d(5))

def sequence_e(n):
    if n == 1:
        return 3
    elif n == 2:
        return 5
    else:
        return sequence_e(n - 2) + 1

print(sequence_e(4))
