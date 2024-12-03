import re

TaskFile = open("AdventOfCode2024/5thInputToTask.txt","r")

def How_many_mul(file):
    can = True
    count = 0
    for line in file:
        Correct_mul = re.findall(r"don't|do|mul\(\d{1,3},\d{1,3}\)", line)
        for i in Correct_mul:
            print(i)
            if i == "don't":
                can = False
            elif i == "do":
                can = True
            elif can == True:
                line = list(map(int, i[4:-1].split(',')))
                count += (line[0]*line[1])
    return count

print(How_many_mul(TaskFile))