import re

TaskFile = open("AdventOfCode2024/7thInputToTask.txt","r")

def Is_Xmas_Horizontal(HorizontalList):
    count = 0
    Check = "XMAS"
    for i in range(len(HorizontalList)-3):
        if (HorizontalList[i]+HorizontalList[i+1]+HorizontalList[i+2]+HorizontalList[i+3]) == Check:
            count += 1
    return count


def Count_Xmas(file):
    c = []
    cL = []
    count = 0
    
    #Horizontal
    for lines in file:
        line = list(map(str, lines.strip()))
        c.append(line)
        count += Is_Xmas_Horizontal(line)
        count += Is_Xmas_Horizontal(line[::-1])
    
    #Vertical
    for i in range(len(c)-3):
        Vertical = zip(c[i], c[i+1], c[i+2], c[i+3])
        for i in Vertical:
            count += Is_Xmas_Horizontal(i)
            count += Is_Xmas_Horizontal(i[::-1])
    
    #Diagonal Rigth
    for i in range(len(c)-3):
        DiagonalR = zip(c[i], c[i+1][1:],c[i+2][2:], c[i+3][3:])
        for i in DiagonalR:
            count += Is_Xmas_Horizontal(i)
            count += Is_Xmas_Horizontal(i[::-1])
    
    #Diagonal Left
    for i in c:
        cL.append(i[::-1])
    for i in range(len(cL)-3):
        DiagonalL = zip(cL[i], cL[i+1][1:],cL[i+2][2:], cL[i+3][3:])
        for i in DiagonalL:
            count += Is_Xmas_Horizontal(i)
            count += Is_Xmas_Horizontal(i[::-1])
    return count

print(Count_Xmas(TaskFile))