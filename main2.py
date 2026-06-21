#Python Program Branch 2

import random

def play_guessing_game():
    print("Welcome to the Guessing Game!")
    # Generate a random integer between 1 and 20
    secret_number = random.randint(1, 20)
    attempts = 0
    
    # Loop continuously until the user gets it right
    while True:
        try:
            guess = int(input("Guess a number between 1 and 20: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You found it in {attempts} attempts.")
                break # Exit the game loop
        except ValueError:
            print("Invalid input! Please enter a whole number.")

# Run the game function
if __name__ == "__main__":
    play_guessing_game()

