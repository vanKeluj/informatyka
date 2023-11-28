
def Trójkąt(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        p=(a+b+c)/2
        print("Pole wynosi:", (p*(p-a)(p-b)(p-c))**(1/2))
    else:
        print("ztych ścian nie można zrobić trójkąta")

Trójkąt(3, 5, 9)
Trójkąt(3, 4, 6)