def parseFile():
  with open("day-4\input.txt") as inputFile:
    lines = []
    data = inputFile.readlines()
    for i in range(len(data)):
      lines.append(data[i].strip())
  return lines