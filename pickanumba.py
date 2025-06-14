import random
'''A simple Number guessing game
'''

def random_num():
  '''the random number generator'''
  random_num = rand.int(1,9)
  return random_num
  
def user_guess():
  '''The players guess'''
  user_guess = input("Take a guess*enter a number(1-9)*: ")
  if user_guess.isdigit() and in range(1,9):
    return user_guess
  else:
    print("try again...")
    return ""

def number_validator(random_num,user_guess):
  '''number check???'''
  if user_guess=random_num+1 or user_guess=random_num-1:
    print("almost!!!")
    return True
  elif int(random_num)==int(user_guess):
    print("Lucky Bastard!!!")
    return False
  else:
    print("Keep Trying")
    return True

def main():
  '''where the magic happens'''
random_number = random_num()
player_guess = user_guess()
number_validator(random_number, player_guess)
if __name__ == "__main__":
  main()
