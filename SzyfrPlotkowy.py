def szyfr(word, key):
  workword = "".join([litera.upper() for litera in word])

  numofletters = len(workword)
  plotek = [['' for _ in range(key)] for _ in range(numofletters)]
  
  dir = 1
  index = 0
  line = 0

  while workword:
    letter = workword[0]
    plotek[index][line] = letter
    index += 1

    if line == key - 1:
      dir = -1
    elif line == 0:
      dir = 1

    line += dir

    workword = workword[1:]

  returnWord = ''
  for line in range(key):
    for linePlotek in plotek:
      returnLetter = linePlotek[line]
      if returnLetter != ' ':
        returnWord += returnLetter

  return returnWord


def deszyfr(word, key):
  workword = ""

  numofletters = len(word)
  plotek = [['' for _ in range(key)] for _ in range(numofletters)]
  
  dir = 1
  index = 0
  line = 0
  numofletterstemp = numofletters

  while numofletterstemp:
    plotek[index][line] = '*'
    index += 1

    if line == key - 1:
      dir = -1
    elif line == 0:
      dir = 1
    
    line += dir
    
    numofletterstemp -= 1

  while word:
    for indeks in range(key):
      for wiersz in plotek:
        try:
          if wiersz.index('*') == indeks:
            wiersz[indeks] = word[0]
            word = word[1:]
        except:
          pass

  dir = 1
  index = 0
  line = 0
  numofletterstemp = 0

  while numofletterstemp < numofletters:
    workword += plotek[index][line]
    index += 1

    if line == key - 1:
      dir = -1
    elif line == 0:
      dir = 1

    line += dir

    numofletterstemp += 1

  return workword
      

print(szyfr('KRYPTOANALIZA', 3))
print(deszyfr('KTAARPONLZYAI', 3))
