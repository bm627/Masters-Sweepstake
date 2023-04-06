import requests
import json
import time 

def updateScore(chosenPlayers):
  url = "https://www.golfchannel.com/api/v2/events/19956/leaderboard"

  payload = ""
  response = requests.request("GET", url, data=payload)

  jsondata = json.loads(response.text)

  playersAndScores = {}

  for i in range(len(jsondata['result']['golfers'])):
      firstName = jsondata['result']['golfers'][i]['firstName']
      lastName = jsondata['result']['golfers'][i]['lastName']
      score = jsondata['result']['golfers'][i]['overallPar']
      name = firstName + ' ' + lastName
      newDict = {name:score}
      playersAndScores.update(newDict)

  #Running through the dictionary, extracting value/score for 6 chosen players
  scoreList = []

  for player in chosenPlayers:
    if player in playersAndScores:
      print(player,playersAndScores.get(player))
      scoreList.append(playersAndScores.get(player))
    else:
      pass

  #Converting list of string scores to integer scores, sorting, taking top 4 and adding to give total
  scoreInts = []
  for score in scoreList:
    scoreInts.append(int(score))

  scoreInts.sort()

  topFour = scoreInts[0:4]

  total = sum(topFour)
  print(total)

chosenPlayers = ['Rory McIlroy', 'Jordan Spieth', 'Tommy Fleetwood', 'Jason Day', 'Min Woo Lee', 'Brooks Koepka']

while __name__ == "__main__":
    updateScore(chosenPlayers)
    time.sleep(300)