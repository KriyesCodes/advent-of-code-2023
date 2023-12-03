def parseFile():
  with open("day-1\part2Example.txt") as inputFile:
    lines = []
    data = inputFile.readlines()
    for i in range(len(data)):
      lines.append(data[i].strip())
  return lines


print(parseFile())
