def parseFile():
  with open("day-1\example.txt") as inputFile:
    lines = inputFile.readlines()
  return lines


def sumCalibrationValues(document):
  sum = 0

  for i in range(len(document)):
    calibrationValue = ''

    for j in range(len(document[i])):
      if document[i][j].isdigit():
        calibrationValue += document[i][j]
        break
    for j in range(len(document[i])-1, -1, -1):
      if document[i][j].isdigit():
        calibrationValue += document[i][j]
        break

    sum += int(calibrationValue)

  return sum


print(sumCalibrationValues(parseFile()))