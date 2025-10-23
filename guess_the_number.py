import random
import time
from datetime import datetime

class NumberGuessingGame:
    """Enhanced Number Guessing Game with multiple features"""
    
    def __init__(self):
        """Initialize game statistics and settings"""
        self.total_games = 0
        self.games_won = 0
        self.games_lost = 0
        self.best_score = float('inf')
        self.total_attempts = 0
        self.game_history = []
        self.player_name = ""
        self.current_streak = 0
        self.best_streak = 0
        
    def display_banner(self):
        """Display welcome banner"""
        print("\n" + "=" * 60)
        print("🎮" + " " * 15 + "GUESS THE NUMBER GAME" + " " * 16 + "🎮")
        print("=" * 60)
        
    def get_player_name(self):
        """Get and store player name"""
        if not self.player_name:
            self.player_name = input("\n👤 Enter your name: ").strip()
            if not self.player_name:
                self.player_name = "Player"
        print(f"\n👋 Welcome, {self.player_name}!")
        
    def choose_difficulty(self):
        """Let player choose difficulty level"""
        print("\n📊 Choose Difficulty Level:")
        print("=" * 60)
        print("1. 🟢 Easy   - Numbers 1-50, 10 attempts, 3 hints")
        print("2. 🟡 Medium - Numbers 1-100, 7 attempts, 2 hints")
        print("3. 🔴 Hard   - Numbers 1-200, 5 attempts, 1 hint")
        print("4. 💀 Expert - Numbers 1-500, 7 attempts, 0 hints")
        print("=" * 60)
        
        while True:
            choice = input("\nSelect difficulty (1-4): ").strip()
            if choice == '1':
                return {'range': 50, 'attempts': 10, 'hints': 3, 'name': 'Easy', 'points': 100}
            elif choice == '2':
                return {'range': 100, 'attempts': 7, 'hints': 2, 'name': 'Medium', 'points': 250}
            elif choice == '3':
                return {'range': 200, 'attempts': 5, 'hints': 1, 'name': 'Hard', 'points': 500}
            elif choice == '4':
                return {'range': 500, 'attempts': 7, 'hints': 0, 'name': 'Expert', 'points': 1000}
            else:
                print("❌ Invalid choice! Please select 1-4.")
    
    def get_hint(self, secret_number, hints_remaining, game_range):
        """Provide different types of hints"""
        if hints_remaining <= 0:
            print("❌ No hints remaining!")
            return hints_remaining
        
        print("\n💡 Available Hints:")
        print("1. Even/Odd hint")
        print("2. Divisibility hint")
        print("3. Range narrowing hint")
        
        choice = input(f"Choose hint (1-3) [{hints_remaining} hints left]: ").strip()
        
        if choice == '1':
            parity = "even" if secret_number % 2 == 0 else "odd"
            print(f"✨ Hint: The number is {parity}!")
        elif choice == '2':
            divisors = [3, 5, 7, 10]
            divisible_by = [d for d in divisors if secret_number % d == 0]
            if divisible_by:
                div = random.choice(divisible_by)
                print(f"✨ Hint: The number is divisible by {div}!")
            else:
                print(f"✨ Hint: The number is NOT divisible by 3, 5, 7, or 10!")
        elif choice == '3':
            quarter = game_range // 4
            if secret_number <= quarter:
                print(f"✨ Hint: The number is in the range 1-{quarter}!")
            elif secret_number <= quarter * 2:
                print(f"✨ Hint: The number is in the range {quarter+1}-{quarter*2}!")
            elif secret_number <= quarter * 3:
                print(f"✨ Hint: The number is in the range {quarter*2+1}-{quarter*3}!")
            else:
                print(f"✨ Hint: The number is in the range {quarter*3+1}-{game_range}!")
        else:
            print("❌ Invalid hint choice!")
            return hints_remaining
        
        return hints_remaining - 1
    
    def calculate_score(self, attempts, max_attempts, difficulty_points, time_taken, hints_used, max_hints):
        """Calculate score based on performance"""
        # Base score from difficulty
        score = difficulty_points
        
        # Bonus for fewer attempts (up to 50% bonus)
        attempt_ratio = 1 - (attempts / max_attempts)
        score += int(difficulty_points * 0.5 * attempt_ratio)
        
        # Time bonus (faster = better, max 25% bonus)
        if time_taken < 30:
            time_bonus = int(difficulty_points * 0.25 * (1 - time_taken / 30))
            score += time_bonus
        
        # Penalty for using hints
        hint_penalty = int(difficulty_points * 0.1 * hints_used)
        score -= hint_penalty
        
        return max(score, 0)
    
    def play_game(self):
        """Main game logic with enhanced features"""
        self.total_games += 1
        
        # Get difficulty settings
        difficulty = self.choose_difficulty()
        game_range = difficulty['range']
        max_attempts = difficulty['attempts']
        hints_remaining = difficulty['hints']
        difficulty_name = difficulty['name']
        base_points = difficulty['points']
        
        # Generate secret number
        secret_number = random.randint(1, game_range)
        attempts = 0
        hints_used = 0
        guesses = []
        start_time = time.time()
        
        print("\n" + "=" * 60)
        print(f"🎯 Difficulty: {difficulty_name}")
        print(f"📍 Range: 1-{game_range}")
        print(f"🎫 Attempts: {max_attempts}")
        print(f"💡 Hints: {hints_remaining}")
        print("=" * 60)
        print(f"\n🔮 I'm thinking of a number between 1 and {game_range}...")
        print("💭 Type 'hint' to use a hint, 'quit' to give up")
        
        # Game loop
        while attempts < max_attempts:
            attempts += 1
            remaining = max_attempts - attempts + 1
            
            # Display progress bar
            progress = "█" * attempts + "░" * (max_attempts - attempts)
            print(f"\n[{progress}] Attempt {attempts}/{max_attempts}")
            
            # Get player input
            user_input = input(f"Enter your guess: ").strip().lower()
            
            # Check for special commands
            if user_input == 'quit':
                print(f"\n😢 You gave up! The number was {secret_number}")
                self.games_lost += 1
                return
            
            if user_input == 'hint':
                if hints_remaining > 0:
                    hints_remaining = self.get_hint(secret_number, hints_remaining, game_range)
                    hints_used += 1
                    attempts -= 1  # Don't count hint usage as an attempt
                else:
                    print("❌ No hints available!")
                    attempts -= 1
                continue
            
            # Validate guess
            try:
                guess = int(user_input)
            except ValueError:
                print("❌ Please enter a valid number!")
                attempts -= 1
                continue
            
            if guess < 1 or guess > game_range:
                print(f"❌ Please guess between 1 and {game_range}!")
                attempts -= 1
                continue
            
            # Store guess
            guesses.append(guess)
            
            # Check the guess
            if guess == secret_number:
                end_time = time.time()
                time_taken = round(end_time - start_time, 2)
                
                # Calculate score
                score = self.calculate_score(attempts, max_attempts, base_points, 
                                            time_taken, hints_used, difficulty['hints'])
                
                # Update statistics
                self.games_won += 1
                self.total_attempts += attempts
                self.current_streak += 1
                if self.current_streak > self.best_streak:
                    self.best_streak = self.current_streak
                if attempts < self.best_score:
                    self.best_score = attempts
                
                # Store game result
                self.game_history.append({
                    'difficulty': difficulty_name,
                    'attempts': attempts,
                    'time': time_taken,
                    'score': score,
                    'won': True,
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                
                # Victory message
                print("\n" + "🎉" * 30)
                print(f"🏆 CONGRATULATIONS, {self.player_name}! 🏆")
                print("🎉" * 30)
                print(f"✨ You guessed it in {attempts} attempts!")
                print(f"⏱️  Time taken: {time_taken} seconds")
                print(f"💰 Score: {score} points")
                print(f"🔥 Current streak: {self.current_streak}")
                if hints_used > 0:
                    print(f"💡 Hints used: {hints_used}")
                print("🎉" * 30)
                
                return
            
            # Provide feedback
            diff = abs(guess - secret_number)
            
            if guess < secret_number:
                if diff <= 5:
                    print(f"🔥 Very close! Too low! ({remaining - 1} left)")
                elif diff <= 10:
                    print(f"📈 Close! Too low! ({remaining - 1} left)")
                else:
                    print(f"📈 Too low! ({remaining - 1} left)")
            else:
                if diff <= 5:
                    print(f"🔥 Very close! Too high! ({remaining - 1} left)")
                elif diff <= 10:
                    print(f"📉 Close! Too high! ({remaining - 1} left)")
                else:
                    print(f"📉 Too high! ({remaining - 1} left)")
            
            # Show guess history
            if len(guesses) > 1:
                print(f"📝 Your guesses: {', '.join(map(str, guesses[-5:]))}")
        
        # Game over - out of attempts
        end_time = time.time()
        time_taken = round(end_time - start_time, 2)
        
        self.games_lost += 1
        self.total_attempts += attempts
        self.current_streak = 0
        
        self.game_history.append({
            'difficulty': difficulty_name,
            'attempts': attempts,
            'time': time_taken,
            'score': 0,
            'won': False,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        
        print("\n" + "💔" * 30)
        print(f"😢 Game Over, {self.player_name}!")
        print(f"🎯 The number was: {secret_number}")
        print(f"📝 Your guesses: {', '.join(map(str, guesses))}")
        print("💔" * 30)
    
    def display_statistics(self):
        """Display comprehensive game statistics"""
        if self.total_games == 0:
            print("\n📊 No games played yet!")
            return
        
        win_rate = (self.games_won / self.total_games) * 100
        avg_attempts = self.total_attempts / self.total_games if self.total_games > 0 else 0
        
        print("\n" + "=" * 60)
        print(f"📊 {self.player_name}'s STATISTICS")
        print("=" * 60)
        print(f"🎮 Total Games Played: {self.total_games}")
        print(f"🏆 Games Won: {self.games_won}")
        print(f"😢 Games Lost: {self.games_lost}")
        print(f"📈 Win Rate: {win_rate:.1f}%")
        print(f"⭐ Best Score (fewest attempts): {self.best_score if self.best_score != float('inf') else 'N/A'}")
        print(f"📊 Average Attempts: {avg_attempts:.1f}")
        print(f"🔥 Current Streak: {self.current_streak}")
        print(f"🏅 Best Streak: {self.best_streak}")
        print("=" * 60)
        
        if self.game_history:
            print("\n📜 Recent Game History (last 5 games):")
            print("-" * 60)
            for i, game in enumerate(self.game_history[-5:], 1):
                result = "✅ WON" if game['won'] else "❌ LOST"
                print(f"{i}. {game['timestamp']} | {game['difficulty']} | "
                      f"{result} | Attempts: {game['attempts']} | "
                      f"Time: {game['time']}s | Score: {game['score']}")
            print("-" * 60)
    
    def show_leaderboard(self):
        """Display leaderboard of best performances"""
        if not self.game_history:
            print("\n🏆 No games in history yet!")
            return
        
        won_games = [g for g in self.game_history if g['won']]
        if not won_games:
            print("\n🏆 No winning games yet!")
            return
        
        # Sort by score
        sorted_games = sorted(won_games, key=lambda x: x['score'], reverse=True)
        
        print("\n" + "=" * 60)
        print("🏆 LEADERBOARD - TOP 5 SCORES")
        print("=" * 60)
        for i, game in enumerate(sorted_games[:5], 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "🏅"
            print(f"{medal} {i}. {game['score']} pts | {game['difficulty']} | "
                  f"{game['attempts']} attempts | {game['time']}s | {game['timestamp']}")
        print("=" * 60)
    
    def show_menu(self):
        """Display main menu"""
        print("\n" + "=" * 60)
        print("📋 MAIN MENU")
        print("=" * 60)
        print("1. 🎮 Play Game")
        print("2. 📊 View Statistics")
        print("3. 🏆 View Leaderboard")
        print("4. 📖 How to Play")
        print("5. 🚪 Exit")
        print("=" * 60)
    
    def show_instructions(self):
        """Display game instructions"""
        print("\n" + "=" * 60)
        print("📖 HOW TO PLAY")
        print("=" * 60)
        print("1. Choose a difficulty level")
        print("2. The computer will think of a random number")
        print("3. Try to guess the number within the given attempts")
        print("4. After each guess, you'll get feedback:")
        print("   - 'Too high' means guess lower")
        print("   - 'Too low' means guess higher")
        print("   - 'Very close' means you're within 5 numbers!")
        print("5. Use hints wisely to narrow down the range")
        print("6. Type 'hint' to use a hint, 'quit' to give up")
        print("7. Score more points by:")
        print("   - Using fewer attempts")
        print("   - Guessing faster")
        print("   - Using fewer hints")
        print("=" * 60)
    
    def run(self):
        """Main game loop"""
        self.display_banner()
        self.get_player_name()
        
        while True:
            self.show_menu()
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                self.play_game()
            elif choice == '2':
                self.display_statistics()
            elif choice == '3':
                self.show_leaderboard()
            elif choice == '4':
                self.show_instructions()
            elif choice == '5':
                print(f"\n👋 Thanks for playing, {self.player_name}! Goodbye!")
                if self.total_games > 0:
                    print(f"🎮 You played {self.total_games} game(s) with a "
                          f"{(self.games_won/self.total_games)*100:.1f}% win rate!")
                break
            else:
                print("❌ Invalid choice! Please select 1-5.")
            
            input("\nPress Enter to continue...")


# Run the game
if __name__ == "__main__":
    game = NumberGuessingGame()
    game.run()