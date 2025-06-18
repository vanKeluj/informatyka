import math
def szyfr(word, key):
  returnWord = ''
  kolumns = []
  workword = "".join([litera.upper() for litera in word])
  repeat = math.ceil(len(workword)/len(key))
  
  for i in range(repeat):
    tempList = []
    for j in workword[:len(key)]:
      tempList.append(j)
    kolumns.append(tempList)
    workword = workword[5:]

  for i in range(len(key)):
    for j in range(repeat):
      try:
        returnWord += kolumns[j][key[i]]
      except:
        pass
    
  return returnWord


def deszyfr(word, key):
  workword = "".join([litera.upper() for litera in word])
  workword2 = "".join([litera.upper() for litera in word])
  tempList = []
  print(tempList)

  kolumns = []
  repeat = math.ceil(len(workword)/len(key))

  for i in range(math.ceil(len(workword)/len(key))):
    for j in workword[:len(key)]:
      tempList.append('*')

    kolumns.append(tempList)
    tempList = []

    workword = workword[len(key):]

  returnWord = ''
  for i in range(5):
    for j in range(repeat):
      try:
        kolumns[j][key[i]] = workword2[:1]
        workword2 = workword2[1:]
      except:
        pass
  for i in kolumns:
    for j in i:
      returnWord += j

  return returnWord


print(szyfr('KRYPTOANALIZA', [2,1,4,0,3]))
print(deszyfr('CŚIPWIEZAZOBAHYIZNUIĆEOAURICWZRCLMAM', [3, 2, 0, 1]))