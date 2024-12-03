import re

TaskFile = open("AdventOfCode2024/5thInputToTask.txt","r")

def How_many_mul(file):
    count = 0
    for line in file:
        Correct_mul = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
        for i in Correct_mul:
            line = list(map(int, i[4:-1].split(',')))
            count += (line[0]*line[1])
            print(line,line[0]*line[1],count)
    return count

print(How_many_mul(TaskFile))