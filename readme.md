🎮 Advanced Number Guessing Game - Enhanced Edition
View your enhanced game
New Features Added:
1. Multiple Difficulty Levels 🎯

Easy: 1-50 range, 10 attempts, 3 hints
Medium: 1-100 range, 7 attempts, 2 hints
Hard: 1-200 range, 5 attempts, 1 hint
Expert: 1-500 range, 7 attempts, 0 hints

2. Advanced Hint System 💡

Even/Odd hint: Tells if number is even or odd
Divisibility hint: Shows what the number is divisible by
Range narrowing: Narrows down to 1/4 of the range

3. Dynamic Scoring System 💰

Base points based on difficulty
Bonus for using fewer attempts
Speed bonus for quick guesses
Penalty for using hints
Points tracked across all games

4. Proximity Feedback 🔥

"Very close" when within 5 numbers
"Close" when within 10 numbers
Regular feedback for farther guesses

5. Player Profile & Statistics 📊

Player name tracking
Total games played
Win/loss record
Win rate percentage
Average attempts per game
Best score (fewest attempts)
Current winning streak
Best winning streak

6. Game History 📜

Timestamp for each game
Difficulty level played
Number of attempts
Time taken
Score achieved
Win/loss status

7. Leaderboard 🏆

Top 5 high scores
Sortable by points
Shows difficulty, attempts, and time

8. Visual Enhancements 🎨

Progress bar showing attempts used
Emojis for better visual feedback
Color-coded messages
Professional formatting
Guess history display

9. Menu System 📋

Play game
View statistics
View leaderboard
Instructions/How to play
Exit game

10. Additional Features ⭐

Time tracking for each game
Special commands ('hint', 'quit')
Input validation
Guess history (last 5 guesses shown)
Session summary on exit

How to Run:
bashpython advanced_guess_game.py
Or:
bashpython3 advanced_guess_game.py
```

### **Gameplay Example:**
```
🎮 WELCOME TO GUESS THE NUMBER GAME 🎮
👤 Enter your name: Alex

📋 MAIN MENU
1. 🎮 Play Game
2. 📊 View Statistics
3. 🏆 View Leaderboard
4. 📖 How to Play
5. 🚪 Exit

Enter your choice: 1

📊 Choose Difficulty Level:
1. 🟢 Easy   - Numbers 1-50, 10 attempts, 3 hints
2. 🟡 Medium - Numbers 1-100, 7 attempts, 2 hints
3. 🔴 Hard   - Numbers 1-200, 5 attempts, 1 hint
4. 💀 Expert - Numbers 1-500, 7 attempts, 0 hints

Select difficulty: 2

🎯 Difficulty: Medium
📍 Range: 1-100
🎫 Attempts: 7
💡 Hints: 2

[█░░░░░░] Attempt 1/7
Enter your guess: 50
📈 Too low! (6 left)

[██░░░░░] Attempt 2/7
Enter your guess: hint

💡 Available Hints:
1. Even/Odd hint
2. Divisibility hint
3. Range narrowing hint

Choose hint (1-3) [2 hints left]: 1
✨ Hint: The number is even!

[██░░░░░] Attempt 2/7
Enter your guess: 76
🔥 Very close! Too high! (6 left)

[███░░░░] Attempt 3/7
Enter your guess: 72
🏆 CONGRATULATIONS! 🏆
✨ You guessed it in 3 attempts!
⏱️  Time taken: 18.5 seconds
💰 Score: 350 points
🔥 Current streak: 1
Object-Oriented Design:
The code uses a class-based structure with:

Organized methods for different features
Persistent state across games
Easy to extend and modify
Professional code organization

Requirements:

Python 3.x
Built-in libraries only (no installation needed)