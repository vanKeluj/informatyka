import math

x = int(2.5)
y = int(3)

def cos(x,y):
    A = int(3)
    B = int(4)
    C = int(-4)

    d = (A*x + B*y + C)/(A**2+B**2)**(1/2)
    
    if d == 0:
        return True
    else:
        return False

print(cos(x,y))
