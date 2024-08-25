import random

print("Welcome to the Word Guessing Game!")

def GuessTheWord ():
    word = random.choice(["stop", "pots", "spot", "tops"])
    guess = ""
    
    while guess != word:
        print("I'm thinking of a word. Here's your hint: _ _ _ _ (OPST)")
        guess=input("Enter your guess: ").lower()
    
    if guess == word:
        print(f"Congratulations! You guessed the word '{word}'!")
    else:
        print("That's not correct. Try again!")
        
GuessTheWord()