import re

TaskFile = open("AdventOfCode2024/7thInputToTask.txt","r")

def Is_There_Xmas(Characters):
    count = 0
    Check = "XMAS"
    for i in range(len(Characters)-3):
        if (Characters[i]+Characters[i+1]+Characters[i+2]+Characters[i+3]) == Check:
            count += 1
    return count


def Count_Xmas(file):
    c = [] #All characters Left to Right
    cR = [] #All characters Right to Left
    count = 0
    
    #Check if there is XMAS Horizontal
    for lines in file:
        CharactersIn_line = list(map(str, lines.strip()))
        c.append(CharactersIn_line)
        count += Is_There_Xmas(CharactersIn_line)
        count += Is_There_Xmas(CharactersIn_line[::-1])
    
    #Check if there is XMAS Vertical
    for i in range(len(c)-3):
        Vertical = zip(c[i], c[i+1], c[i+2], c[i+3])
        for characters in Vertical:
            count += Is_There_Xmas(characters)
            count += Is_There_Xmas(characters[::-1])
    
    #Check if there is XMAS Diagonal from Left to Rigth
    for i in range(len(c)-3):
        DiagonalR = zip(c[i], c[i+1][1:],c[i+2][2:], c[i+3][3:])
        for characters in DiagonalR:
            count += Is_There_Xmas(characters)
            count += Is_There_Xmas(characters[::-1])
    
    #Check if there is XMAS Diagonal from Right to Left
    for i in c:
        cR.append(i[::-1])
    for i in range(len(cR)-3):
        DiagonalL = zip(cR[i], cR[i+1][1:],cR[i+2][2:], cR[i+3][3:])
        for characters in DiagonalL:
            count += Is_There_Xmas(characters)
            count += Is_There_Xmas(characters[::-1])
    return count

print(Count_Xmas(TaskFile))