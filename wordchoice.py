import random 
word=random.choice(["apple","banana","cherry","blueberry"])
guess=""

while guess != word:
    guess=input('entere your guess:').lower()
  
  # if the user guesses too lower, tell them to guess higher, if they guess 
  # too high, tell them to guess lower, and if they get it correct tell 
  # them they've won
    if guess != word:
        print("u won word ")
    else:
     print("You loose!")
     break
print(f"the word was{word}.")