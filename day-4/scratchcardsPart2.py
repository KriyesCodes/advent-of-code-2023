def parseFile():
  with open("day-4\input.txt") as inputFile:
    lines = []
    data = inputFile.readlines()
    for i in range(len(data)):
      lines.append(data[i].strip())
  return lines

def calculateCards(cardsData):
  cardInstances = {}
  for card in cardsData:
    cardInstancesKey = int(card.split(":")[0].split()[1])
    cardInstances[cardInstancesKey] = 1

  for card in cardsData:
    cardKey = int(card.split(":")[0].split()[1])
    winningNumbers = list(map(int, card.split(":")[1].split("|")[0].split()))
    acquiredNumbers = list(map(int, card.split(":")[1].split("|")[1].split()))

    matches = 0
    
    for number in acquiredNumbers:
      if number in winningNumbers:
        matches += 1

    for i in range(cardInstances[cardKey]):
      for i in range(cardKey+1, cardKey + matches + 1):
          cardInstances[i] += 1
    

  return sum(cardInstances.values())

print(calculateCards(parseFile()))