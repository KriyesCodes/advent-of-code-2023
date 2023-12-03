def parseFile():
  with open("day-1\input.txt") as inputFile:
    lines = []
    data = inputFile.readlines()
    for i in range(len(data)):
      lines.append(data[i].strip())
  return lines

def sumCalibrationValues(document):
  numbers = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
  }

  sum = 0

  for line in document:
    calibrationValue = ''
    for startIndex in range(len(line)):
      numFound = False

      if line[startIndex].isdigit():
        calibrationValue += line[startIndex]
        numFound = True
        break

      for endIndex in range(startIndex, len(line)+1):
        if line[startIndex:endIndex] in numbers:
          calibrationValue += numbers[line[startIndex:endIndex]]
          numFound = True

      if numFound:
        break

    for endIndex in range(len(line), -1, -1):
      numFound = False

      if line[endIndex-1].isdigit():
        calibrationValue += line[endIndex-1]
        numFound = True
        break

      for startIndex in range(endIndex, -1, -1):
        if line[startIndex:endIndex] in numbers:
          calibrationValue += numbers[line[startIndex:endIndex]]
          numFound = True

      if numFound:
        break
    
    print(int(calibrationValue))
    sum += int(calibrationValue)
          
  return sum
    

print(sumCalibrationValues(parseFile()))