P = [3,-2]
A = [2,-3]
B = [4,-1]

AB = (((B[0] - A[0])**2) + ((B[1] - A[1])**2))**(1/2)
AP = (((P[0] - A[0])**2) + ((P[1] - A[1])**2))**(1/2)
PB = (((B[0] - P[0])**2) + ((B[1] - P[1])**2))**(1/2)
center = PB-AP
suma = AP+PB
if suma == AB:
    print("Punkt P znajduje się na odcinku AB")
    if center == 0:
        print("Punkt P jest w środku")
    else:
        print("Punkt P nie jest w środku")
else:
    print("Punkt P nie znajduje się na odcinku AB") 