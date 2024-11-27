file_a = open("anagram.txt",'r')
file_b = open("anagram.txt",'r')
output_file_a = open("odp_4a.txt",'w')
output_file_b = open("odp_4b.txt",'w')

def are_anagrams(s1, s2):
    # Bez spacji i z małych liter
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()

    # czy są takiej samej długości
    if len(s1) != len(s2):
        return False

    # Sort both strings
    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)
    
    if sorted_s1 != sorted_s2:
        return False
    else:
        return True


def slowa_tylesamo_liter(file):
    for line in file:
        line = line.strip()
        words = line.split()
        if all(len(words[0]) == len(word) for word in words):
            output_file_a.write(line +"\n")
            
def slowa_to_anagramy(file):
    for line in file:
        line = line.strip()
        words = line.split()
        if all(are_anagrams(words[0],word) for word in words):
            output_file_b.write(line +"\n")
        
slowa_tylesamo_liter(file_a)
slowa_to_anagramy(file_b)
