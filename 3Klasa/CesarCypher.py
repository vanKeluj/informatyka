def CesarCipher(text, shift):
  Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  newAlphabet = Alphabet[shift:]+Alphabet[:shift]
  TextToList = []
  wordtoReturn= ''
  for i in text:
      TextToList.append(i.upper())

  for i in range(len(TextToList)):
    if TextToList[i] != ' ':
      TextToList[i] = newAlphabet[Alphabet.index(TextToList[i].lower())].upper()

  for i in TextToList:
    wordtoReturn += i
  
  return wordtoReturn

def deCesarCipher(text, shift):
  Alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  newAlphabet = Alphabet[shift:]+Alphabet[:shift]
  TextToList = []
  wordtoReturn= ''
  for i in text:
    TextToList.append(i.upper())

  for i in range(len(TextToList)):
    if TextToList[i] != ' ':
     TextToList[i] = Alphabet[newAlphabet.index(TextToList[i].lower())].upper()
  
  for i in TextToList:
    wordtoReturn += i

  return wordtoReturn


print(CesarCipher('KLAMSTWO MA KROTKIE NOGI', 9))
print(deCesarCipher('TUJVBCFXVJTAXCTRNWXPR', 9))

