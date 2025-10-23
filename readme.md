🎮 Guess the Number Game
View your game
How It Works:

Random Number Generation: The game picks a secret number between 1 and 100 using random.randint()
Game Loop: Players get 7 attempts to guess the number
Feedback System: After each guess, the game tells you if you're too high or too low
Input Validation: The game checks that inputs are valid numbers between 1-100
Win/Lose Conditions:

Win by guessing correctly
Lose if you run out of attempts


Replay Option: After each game, you can choose to play again

How to Run:
Option 1 - Using Terminal/Command Prompt:
bashpython guess_the_number.py
Option 2 - Using Python IDLE or any IDE:

Open the file in your Python editor
Press F5 (or click Run)

Option 3 - Direct Python command:
bashpython3 guess_the_number.py

### **Requirements:**
- Python 3.x installed on your computer
- No additional libraries needed (uses built-in `random` module)

### **Sample Gameplay:**
```
🎮 WELCOME TO GUESS THE NUMBER! 🎮
I'm thinking of a number between 1 and 100.
You have 7 attempts to guess it!

Attempt 1/7 - Enter your guess: 50
📈 Too low! Try higher. (6 attempts left)

Attempt 2/7 - Enter your guess: 75
📉 Too high! Try lower. (5 attempts left)

Attempt 3/7 - Enter your guess: 62
🏆 CONGRATULATIONS! You won in 3 attempts!