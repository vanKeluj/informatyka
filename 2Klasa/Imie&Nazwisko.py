#print("{0:10}{1:10}{2:12}".format("Imie","nazwisko","nr Telefonu"))
#print("{0:10}{1:10}{2:12}".format("Mirosław","Handlarz","+48567876576"))
#print("{0:10}{1:10}{2:12}".format("Janusz","Mechanik","+48579253068"))

#print("{0:10}{1:10}{2:12}".format("Imie","nazwisko","Ulica", "nrmieszkania", "nr Telefonu", "miasto", "płec", "wiek"))

informacje = ("Andzrej", "Kierzkowski", "czekoladowa", 15, 6, "czekoladowo", True, 29)
print(informacje)
print("Imie i nazwisko :{0:} {1:}".format(informacje[0]),(informacje[1]))
print("Adres : {0:} {1:}/{2:}, {3:}".format(informacje[2]),(informacje[3]),(informacje[4]),(informacje[5]))
print("Mężczyzna : {0:}, Wiek: {1:}".format(informacje[6]),(informacje[7]))