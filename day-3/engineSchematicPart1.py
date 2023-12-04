def parseInput(PATH):
  with open(PATH) as inputFile:
    data = inputFile.readlines()
    schematic = []
    for i in range(len(data)):
      schematic.append(data[i].strip())

    return schematic

def sumSchematicPartNumbers(schematic):
  sum = 0
  currentNumber = ''
  currentNumberIsPart = False
  lineSums = []

  for y in range(len(schematic)):
    lineSum = 0
    for x in range(len(schematic[y])):
      currentChar = schematic[y][x]

      if ord(currentChar) >= 48 and ord(currentChar) <= 57:
        currentNumber += currentChar

        if (not(currentNumberIsPart)):
          currentNumberIsPart = checkForGearSymbolAround(schematic, x, y)
        
        if (x+1 < len(schematic[y])):
          nextChar = schematic[y][x+1]
          if ord(nextChar) < 48 or ord(nextChar) > 57:
            if currentNumberIsPart:
              sum += int(currentNumber)
              lineSum += int(currentNumber)
              # print("x+1 less than bounds: " + currentNumber) #debug
            currentNumber = ''
            currentNumberIsPart = False
        else:
          if currentNumberIsPart:
              sum += int(currentNumber)
              lineSum += int(currentNumber)
              # print("x+1 more than bounds: " + currentNumber) # debug
          currentNumber = ''
          currentNumberIsPart = False
    lineSums.append(lineSum)

  return lineSums

def checkForGearSymbolAround(schematic, digitX, digitY):
  if not(digitY - 1 < 0):
    if not(digitX - 1 < 0):
      checkChar = schematic[digitY-1][digitX-1]
      if (checkChar != '.') and (ord(checkChar) < 48 or ord(checkChar) > 57):
        return True
    if not(digitX + 1 > len(schematic[digitY - 1]) - 1):
      checkChar = schematic[digitY-1][digitX+1]
      if (checkChar != '.') and (ord(checkChar) < 48 or ord(checkChar) > 57):
        return True
    
    checkChar = schematic[digitY-1][digitX]
    if (checkChar != '.') and (ord(checkChar) < 48 or ord(checkChar) > 57):
        return True

  
  if not(digitY + 1 > len(schematic) - 1):
    if not(digitX - 1 < 0):
      checkChar = schematic[digitY+1][digitX-1]
      if (checkChar != '.') and (ord(checkChar) < 48 or ord(checkChar) > 57):
        return True
    if not(digitX + 1 > len(schematic[digitY + 1]) - 1):
      checkChar = schematic[digitY+1][digitX+1]
      if (checkChar != '.') and (ord(checkChar) < 48 or ord(checkChar) > 57):
        return True
    
    checkChar = schematic[digitY+1][digitX]
    if (checkChar != '.') and (ord(checkChar) < 48 or ord(checkChar) > 57):
        return True
    
  if not(digitX - 1 < 0):
    checkChar = schematic[digitY][digitX-1]
    if (checkChar != '.') and (ord(checkChar) < 48 or ord(checkChar) > 57):
      return True
  if not(digitX + 1 > len(schematic[digitY]) - 1):
    checkChar = schematic[digitY][digitX+1]
    if (checkChar != '.') and (ord(checkChar) < 48 or ord(checkChar) > 57):
      return True
    
  return False


def parseSumsInput(PATH):
  with open(PATH) as inputFile:
    data = inputFile.readlines()
    schematic = []
    for i in range(len(data)):
      schematic.append(data[i].strip())

    return schematic
  
theirLineData = parseSumsInput('day-3\lineSum.txt')
myLineData = sumSchematicPartNumbers(parseInput("day-3\sample4.txt"))

print("{:^15}{:^15}{:^15}{:^15}".format("line num","your line sums", "my line sums", "difference"))
for i in range (len(theirLineData)):
  print("{:^15}{:^15}{:^15}{:^15}".format(i+1, theirLineData[i], myLineData[i], abs(int(theirLineData[i]) - int(myLineData[i]))))