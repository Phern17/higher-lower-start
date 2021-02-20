import art
import game_data
from random import randint

#randomly select an account from game_data
def randomAccountSelector():
  selectedAcc = randint(0, len(game_data.data))
  return game_data.data.pop(selectedAcc)

def printGame(twoIGList):
  acc1 = twoIGList[0]
  acc2 = twoIGList[1]
  print(f'Compare A: {acc1["name"]}, a {acc1["description"]}, from {acc1["country"]}')

  print(art.vs)

  print(f'Against B: {acc2["name"]}, a {acc2["description"]}, from {acc2["country"]}')

def checkGreater(twoIGList):
  acc1 = twoIGList[0]
  acc2 = twoIGList[1]
  A_Wins = False

  #system check which has more followers
  if acc1['follower_count'] > acc2['follower_count']:
    A_Wins = True

  return A_Wins
  
def game():
  print(art.logo)
  twoIGAcc = []
  score = 0
  moreFollower = ""

  #initialize the game with 2 accounts
  for i in range(2):
    twoIGAcc.append(randomAccountSelector())

  printGame(twoIGAcc)

  if checkGreater(twoIGAcc):
    print("Psssst A has more follower")
    moreFollower = "A"
  else:
    print("Psst B has more follower")
    moreFollower = "B"

  userAns = input('Who has more followers? Type A or B: ')

  if userAns.upper() == moreFollower:
    print("Ayyy, You're right.")
  else:
    print("Noob, lol.")
  


game()