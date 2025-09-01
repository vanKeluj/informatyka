months = ["styczeń", "luty", "marzec", "kwiecień", "maj", "czewiec", "lipiec", "sierpień", "wrzesień", "pażdziernik", "listopad", "grudzień"]

with open("TxtFiles/dane1.22.txt", "w") as f:
    for i in months:
        f.write(i +"\n")

with open("TxtFiles/dane1.22.txt", "r") as f:
    for lines in f:
        if lines[0] == "m":
            print(lines)

with open("TxtFiles/wyniki1.22.txt", "w") as f:
    for i in months:
        if len(i) > 8:
            f.write(i +"\n")

with open("TxtFiles/wyniki1.22.txt", "r") as f:
    for lines in f:
        print(lines)


#zadanie 2

Dane = open("TxtFiles/dane1.23.txt", "r")
Wyniki = open("TxtFiles/wyniki1.23.txt", "w")

for lines in Dane:
    lines.replace(" ", ",")
    line = list(map(int, lines.split()))
    if 250 < line[0]*line[1] < 3000:
        Wyniki.write(str(line[0]*line[1]) +"\n")