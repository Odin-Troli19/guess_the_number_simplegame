import random

def play_game():
    """Main function to play the number guessing game"""
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("=" * 50)
    print("🎮 WELCOME TO GUESS THE NUMBER! 🎮")
    print("=" * 50)
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it!")
    print("=" * 50)
    
    # Game loop
    while attempts < max_attempts:
        attempts += 1
        remaining = max_attempts - attempts + 1
        
        # Get player's guess
        try:
            guess = int(input(f"\nAttempt {attempts}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("❌ Please enter a valid number!")
            attempts -= 1  # Don't count invalid inputs
            continue
        
        # Check if guess is valid
        if guess < 1 or guess > 100:
            print("❌ Please guess a number between 1 and 100!")
            attempts -= 1  # Don't count out-of-range guesses
            continue
        
        # Check the guess
        if guess == secret_number:
            print("\n" + "🎉" * 20)
            print(f"🏆 CONGRATULATIONS! You won in {attempts} attempts!")
            print("🎉" * 20)
            return
        elif guess < secret_number:
            print(f"📈 Too low! Try higher. ({remaining - 1} attempts left)")
        else:
            print(f"📉 Too high! Try lower. ({remaining - 1} attempts left)")
    
    # Game over - player ran out of attempts
    print("\n" + "💔" * 20)
    print(f"😢 Game Over! The number was {secret_number}")
    print("💔" * 20)

def main():
    """Main program loop with replay option"""
    
    while True:
        play_game()
        
        # Ask if player wants to play again
        play_again = input("\n🔄 Do you want to play again? (yes/no): ").lower()
        
        if play_again not in ['yes', 'y']:
            print("\n👋 Thanks for playing! Goodbye!")
            break
        print("\n" + "=" * 50 + "\n")

# Run the game
if __name__ == "__main__":
    main()