def parseFile():
  with open("day-4\input.txt") as inputFile:
    lines = []
    data = inputFile.readlines()
    for i in range(len(data)):
      lines.append(data[i].strip())
  return lines

def calculatePoints(cardsData):
  winningNumbers = []
  acquiredNumbers = []
  totalPoints = 0

  for card in cardsData:
    points = 0
    winningNumbers = list(map(int, card.split(":")[1].split("|")[0].split()))
    acquiredNumbers = list(map(int, card.split(":")[1].split("|")[1].split()))
    
    for number in acquiredNumbers:
      if number in winningNumbers:
        if (points != 0):
          points *= 2
        else:
          points += 1

    totalPoints += points

  return totalPoints

print(calculatePoints(parseFile()))