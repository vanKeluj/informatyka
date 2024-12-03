TaskFile = open("AdventOfCode2024/3rdInputToTask.txt","r")

def zadanie(line):
    diffs = [a-b for a,b in zip(line, line[1:])]
    return all(1 <= diff <= 3 for diff in diffs) or all(-1 >= diff >= -3 for diff in diffs)
    

def HowManyIsSafe(file):
    How_many_is_same = 0

    for lines in file:
        line = list(map(int, lines.split()))
        if zadanie(line):
            How_many_is_same += 1
    
    return How_many_is_same 


print(HowManyIsSafe(TaskFile))
