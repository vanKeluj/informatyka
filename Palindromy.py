tekst = "kobyła ma mały bok"

#ignoruje spacj i duże znaki
def palindrom_check(text: str):
    text = text.lower()
    text = text.replace(' ', '')
    return text == text[::-1]

print(f"{tekst} jest palindromiczne = {palindrom_check(tekst)}")

#metoda pana solarza
def palindrom(s):
    dl = len(s)
    i = 0
    while i < (dl/2):
        if s[i] != s[dl-i-1]:
            return False
        else:
            i += 1
    else:
        return True
