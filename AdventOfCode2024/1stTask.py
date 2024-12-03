Input_to_read = open("AdventOfCode2024/1stInputToTaks.txt","r")

def check_distance(file):
    left = []
    right = []
    
    for line in file:
        numbers = line.split()
        left.append(int(numbers[0]))
        right.append(int(numbers[1]))

    left.sort()
    right.sort()
    
    total_distance = sum(abs(left[i] - right[i]) for i in range(len(left)))
    
    return total_distance




print(check_distance(Input_to_read))

