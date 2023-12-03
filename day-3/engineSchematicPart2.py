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
  gears = {}
  currentNumber = ''
  currentNumberIsPart = False

  for y in range(len(schematic)):
    for x in range(len(schematic[y])):
      currentChar = schematic[y][x]

      if ord(currentChar) >= 48 and ord(currentChar) <= 57:
        currentNumber += currentChar

        if (not(currentNumberIsPart)):
          currentNumberIsPart, gearX, gearY = checkForGearSymbolAround(schematic, x, y)
          if currentNumberIsPart:
            lastGear = (gearX, gearY)
        
        if (x+1 < len(schematic[y])):
          nextChar = schematic[y][x+1]
          if ord(nextChar) < 48 or ord(nextChar) > 57:
            if currentNumberIsPart:
              if lastGear in gears:
                gears[lastGear].append(int(currentNumber))
              else:
                gears[lastGear] = [int(currentNumber)]
              print("x+1 less than bounds: " + currentNumber) #debug
            currentNumber = ''
            currentNumberIsPart = False
            lastGear = False
        else:
          if currentNumberIsPart:
              if lastGear in gears:
                gears[lastGear].append(int(currentNumber))
              else:
                gears[lastGear] = [int(currentNumber)]
              print("x+1 more than bounds: " + currentNumber) # debug
          currentNumber = ''
          currentNumberIsPart = False
          lastGear = False

  for key,value in gears.items():
    if (len(value)) == 2:
      gearRatio = value[0] * value[1]
      sum += gearRatio

  return sum

def checkForGearSymbolAround(schematic, digitX, digitY):
  if not(digitY - 1 < 0):
    if not(digitX - 1 < 0):
      checkChar = schematic[digitY-1][digitX-1]
      if (checkChar == '*'):
        return (True, digitX-1, digitY-1)
    if not(digitX + 1 > len(schematic[digitY - 1]) - 1):
      checkChar = schematic[digitY-1][digitX+1]
      if (checkChar == '*'):
        return (True, digitX+1, digitY-1)
    
    checkChar = schematic[digitY-1][digitX]
    if (checkChar == '*'):
        return (True, digitX, digitY-1)

  
  if not(digitY + 1 > len(schematic) - 1):
    if not(digitX - 1 < 0):
      checkChar = schematic[digitY+1][digitX-1]
      if (checkChar == '*'):
        return (True, digitX-1, digitY+1)
    if not(digitX + 1 > len(schematic[digitY - 1]) - 1):
      checkChar = schematic[digitY+1][digitX+1]
      if (checkChar == '*'):
        return (True, digitX+1, digitY+1)
    
    checkChar = schematic[digitY+1][digitX]
    if (checkChar == '*'):
        return (True, digitX, digitY+1)
    
  if not(digitX - 1 < 0):
    checkChar = schematic[digitY][digitX-1]
    if (checkChar == '*'):
      return (True, digitX-1, digitY)
  if not(digitX + 1 > len(schematic[digitY]) - 1):
    checkChar = schematic[digitY][digitX+1]
    if (checkChar == '*'):
      return (True, digitX+1, digitY)
    
  return (False, 0, 0)
  

print(sumSchematicPartNumbers(parseInput()))