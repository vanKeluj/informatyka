
def Func_1(x):
    if x<1:
        return 2*x
    elif x==1:
        return -10
    elif x==3:
        return x**4
    elif x==6:
        return 1.41421356
    else:
        return 0

def Func_2(y):
    if y<7:
        return y**3+1
    elif y==7:
        return y-1
    elif y==9:
        return 5.19615242
    else:
        return 0-8*y

print(Func_1(6))
print(Func_2(3))