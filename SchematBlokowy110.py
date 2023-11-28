x = 0
y = 1
z = 2
i = 0 


while i<5:
    print("i wynosi: ", i)
    j = 0
    while j<5:
        if i%2 == 0:
            if j==1 or j==3:
                print(x)
                j = j+1
            else:
                print(z)
                j = j+1
        if (j+1)%3!=0:
            print(y)
            j = j+1
        else:
            print(x)
            j = j+1
    else:
        i = i+1
else:
    print("stop")