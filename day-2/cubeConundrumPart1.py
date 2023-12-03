def parseFile():
  with open("day-2\input.txt") as inputFile:
    lines = []
    data = inputFile.readlines()
    for i in range(len(data)):
      lines.append(data[i].strip())
  return lines

def sumPossibleGames(games):
  idSum = 0

  for game in games:
    cubesRevealedInGame = {
      'red': [0],
      'blue': [0],
      'green': [0]
    }

    gameId = int(game.split(':')[0].split()[1])
    
    cubeSets = game.split(':')[1].split(';')

    for i in range(len(cubeSets)):
      set = cubeSets[i].split(',')
      for j in range(len(set)):
        set[j] = set[j].strip()
      
        cubesRevealedInGame[set[j].split()[1]].append(int(set[j].split()[0]))

    if (max(cubesRevealedInGame['red']) <= 12) and (max(cubesRevealedInGame['blue']) <= 14) and (max(cubesRevealedInGame['green']) <= 13):
      idSum += gameId

  return idSum

print(sumPossibleGames(parseFile()))