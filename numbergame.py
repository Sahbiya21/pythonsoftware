import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    # Initialize the number of attempts
    attempts = 0
    
    while True:
        # Ask the user for their guess
        user_guess = input("Guess a number between 1 and 100: ")
        
        # Check if the input is a valid number
        if user_guess.isdigit():
            user_guess = int(user_guess)
            
            # Increment the attempts counter
            attempts += 1
            
            # Check if the guess is correct
            if user_guess == number_to_guess:
                print(f"Congratulations! You found the number in {attempts} attempts.")
                break
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        else:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    guess_the_number()
