import re

TaskFile = open("AdventOfCode2024/7thInputToTask.txt","r")

def Is_There_X_mas(Characters):
    count = 0
    Check = ['MMASS', 'SSAMM', 'MSAMS', 'SMASM']
    if Characters in Check:
        count += 1
    return count


def Count_Xmas(file):
    String = ""
    c = []
    cL = []
    count = 0
    
    for lines in file:
        line = list(map(str, lines.strip()))
        c.append(line)
    
    for i in c:
        cL.append(i[::-1])

    for i in range(len(c)-2):
        DiagonalR = zip(c[i], c[i][2:], c[i+1][1:], c[i+2], c[i+2][2:])
        for i in DiagonalR:
            for x in i:
                String += x
            count += Is_There_X_mas(String)
            String = ""

    return count

print(Count_Xmas(TaskFile))