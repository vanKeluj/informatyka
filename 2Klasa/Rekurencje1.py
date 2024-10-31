print ("start")
def wieze_hanoi(krazki, z, do, pomoc):
    if krazki == 1:
        print("Przenieś krążek 1 z", z, "do", do)
        return
    wieze_hanoi(krazki-1, z, pomoc, do)
    print("Przenieś krążek", krazki, "z", z, "do", do)
    wieze_hanoi(krazki-1, pomoc, do, z)

wieze_hanoi(3, 'A', 'B', 'C')
