def are_anagrams(s1, s2):
    # Bez spacji i z małych liter
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # czy są takiej samej długości
    if len(s1) != len(s2):
        return "NIE"

    # Sort both strings
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    
    if sorted_s1 != sorted_s2:
        return "NIE"
    else:
        return "TAK"
    
    
print(are_anagrams("masło masło", "słoma słoma"))  

