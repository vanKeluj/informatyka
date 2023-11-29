print ("start")
def wieze_hanoi(krazki, z, pomocnicza, na):
    if krazki == 1:
        print(f"Przenies krążek 1 z {z} do {na}")
        return
    wieze_hanoi(krazki-1, z, na, pomocnicza)
    print(f"Przenies krążek {krazki} z {z} do {na}")
    wieze_hanoi(krazki-1, pomocnicza, z, na)

wieze_hanoi(3, 'A', 'B', 'C')
