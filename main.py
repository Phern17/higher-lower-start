import art
import game_data
from random import randint

#randomly select an account from game_data
def randomAccountSelector():
  selectedAcc = randint(0, len(game_data.data))
  return game_data.data.pop(selectedAcc)

def printGame(twoIGAcc, winSentence=""):
  print(art.logo)
  acc1 = twoIGAcc[0]
  acc2 = twoIGAcc[1]
  print(f'{winSentence}\nCompare A: {acc1["name"]}, a {acc1["description"]}, from {acc1["country"]}')

  print(art.vs)

  print(f'Against B: {acc2["name"]}, a {acc2["description"]}, from {acc2["country"]}')

def getUserInput():
  userAns = input('Who has more followers? Type A or B: ')
  
  return userAns

def checkGreater(twoIGAcc):
  acc1 = twoIGAcc[0]
  acc2 = twoIGAcc[1]
   
  #system check which has more followers
  if acc1['follower_count'] > acc2['follower_count']:
    return "A"

  else:
    return "B"

def checkGameWin(twoIGAcc, userIn):
  moreFollower = ""
  moreFollower = checkGreater(twoIGAcc)

  if userIn.upper() == moreFollower:
    if moreFollower == "A":
      twoIGAcc.pop(1)
    else:
      twoIGAcc.pop(0)
    return True
  
  else:
    print("Nope. You lose.")
    return False

def playGame(twoIGAcc, userAns):
  score = 0
  resumeGame = True

  #check if user's answer is correct and continue
  while resumeGame:
    if checkGameWin(twoIGAcc, userAns): 
      score += 1
      nextAcc = randomAccountSelector()
      twoIGAcc.append(nextAcc)
      printGame(twoIGAcc, f"Yes, You're correct. Your current score is: {score}") 
      userAns = input('Who has more followers? Type A or B: ')
    else:
      resumeGame = False

def game():
  twoIGAcc = []
  
  #initialize the game with 2 accounts
  for i in range(2):
    twoIGAcc.append(randomAccountSelector())

  printGame(twoIGAcc)
  userAns = getUserInput()
  
  playGame(twoIGAcc, userAns)  

game()