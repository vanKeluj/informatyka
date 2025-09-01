from random import *

alfabet = 'ABCDEF'

def ukryj (tekst):
    wynik = ""
    for t in tekst:
        wynik += t + choice(alfabet)
    return wynik

def porowanj1(T1,T2):
    NieTeSame = 0
    if len(T1) == len(T2):
        for i in range(len(T1)):
            if T1[i] != T2[i]:
                NieTeSame += 1
            elif T1[i] == T2[i]:
                print(T1[i])
        return ("Litery nie zgodne stanowią: "+str((NieTeSame/len(T1))*100)+" %")
    else:
        return "Słowa nie mają takiej samej liczby znaków"


def porowanj2(T1,T2):
    TeSame = 0
    tekst = ''
    if len(T1) < len(T2):
        for i in range(len(T1)):
            if T1[i] == T2[i]:
                TeSame += 1
            elif T1[i] != T2[i]:
                tekst += T1[i]
        for i in range(len(T1)):
            if T1[i] != T2[i]:
                tekst += T2[i]
        return ("Liter zgodnych jest: "+str(TeSame)+' '+ scramble(tekst))
    elif len(T1) > len(T2):
        for i in range(len(T2)):
            if T1[i] == T2[i]:
                TeSame += 1
            elif T1[i] != T2[i]:
                tekst += T1[i]
        for i in range(len(T2)):
            if T1[i] != T2[i]:
                tekst += T2[i]
        return ("Liter zgodnych jest: "+str(TeSame)+' '+ scramble(tekst))

def scramble(tekst):
    for i in range(len(tekst)):
        if tekst.count(tekst[i]) > 1:
            tekst = tekst.replace(tekst[i], "", tekst.count(tekst[i])-1)
    return tekst


#TEKST1 = str(input("Podaj pierwszy tekst: "))
#TEKST2 = str(input("Podaj pierwszy tekst: "))

print(ukryj('KOMPUTER'))
print(porowanj1('INFORMATYK', 'REFORMACJA'))
print(porowanj2('INFORMATYKA', 'REFORMACJA'))