def parseInput():
  with open("input.txt") as inputFile:
    lines = inputFile.readlines()
    schematic = []
    for i in range(len(lines)):
      line = []
      for j in range(len(lines[i])-1):
        line.append(lines[i][j])
      schematic.append(line)
    return schematic

def sumSchematicPartNumbers(schematic):
  sum = 0
  currentNumber = ''
  currentNumberIsPart = False

  for y in range(len(schematic)):
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
              print("x+1 less than bounds: " + currentNumber) #debug
            currentNumber = ''
            currentNumberIsPart = False
        else:
          if currentNumberIsPart:
              sum += int(currentNumber)
              print("x+1 more than bounds: " + currentNumber) # debug
          currentNumber = ''
          currentNumberIsPart = False

  return sum

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
    if not(digitX + 1 > len(schematic[digitY - 1]) - 1):
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
  

print(sumSchematicPartNumbers(parseInput()))