"""
---------------------------------------------------------
Advanced Hangman Game Assignment #3
Author: Devraj Bavan
Date: 2025-07-15

Description:
• Implements Hangman with Easy, Moderate, and Hard levels
• Tracks winners using SQLite database
• Displays Hall of Fame with remaining lives
• Provides clear menus, instructions, and error handling
---------------------------------------------------------
"""

import random
import sqlite3
from tabulate import tabulate

# ================================
# GLOBAL VARIABLES AND CONSTANTS
# ================================
WORD_SETS = {
    "Animal": ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra"],
    "Shape": ["square", "triangle", "rectangle", "circle", "ellipse", "rhombus", "trapezoid"],
    "Place": ["Cairo", "London", "Paris", "Baghdad", "Istanbul", "Riyadh"]
}

HANGMAN_PICS = [
    '''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\\  |
    / \\  |
        ==='''
]

# =========================================
# DATABASE FUNCTIONS: Setup and Management
# =========================================
def initialize_database():
    """Initializes the SQLite database and table for Hall of Fame."""
    conn = sqlite3.connect("hall_of_fame.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS HallOfFame (
                    level TEXT PRIMARY KEY,
                    name TEXT,
                    remaining_lives INTEGER
                )''')
    # Insert default records if table is empty
    for level in ["Easy", "Moderate", "Hard"]:
        c.execute("INSERT OR IGNORE INTO HallOfFame (level, name, remaining_lives) VALUES (?, ?, ?)",
                  (level, "None", 0))
    conn.commit()
    conn.close()

def update_hall_of_fame(level, player_name, remaining_lives):
    """Updates the Hall of Fame if a player achieves a new record."""
    conn = sqlite3.connect("hall_of_fame.db")
    c = conn.cursor()
    c.execute("SELECT remaining_lives FROM HallOfFame WHERE level = ?", (level,))
    current_record = c.fetchone()
    if remaining_lives > current_record[0]:
        c.execute("UPDATE HallOfFame SET name = ?, remaining_lives = ? WHERE level = ?",
                  (player_name, remaining_lives, level))
        print("\n🎉 Congratulations! New Hall of Fame record achieved! 🎉")
    conn.commit()
    conn.close()

def display_hall_of_fame():
    """Displays the current Hall of Fame records in a formatted table."""
    conn = sqlite3.connect("hall_of_fame.db")
    c = conn.cursor()
    c.execute("SELECT * FROM HallOfFame")
    records = c.fetchall()
    print("\n🏆 HALL OF FAME 🏆")
    print(tabulate(records, headers=["Level", "Winner Name", "Remaining Lives"], tablefmt="pretty"))
    conn.close()

# ===============================
# UTILITY AND MENU FUNCTIONS
# ===============================
def get_valid_input(prompt, valid_options):
    """Ensures user input is valid and among the allowed options."""
    while True:
        choice = input(prompt).strip()
        if choice in valid_options:
            return choice
        print("❌ Invalid choice. Please try again.")

def show_about_game():
    """Displays game instructions and level descriptions."""
    print("\n📖 ABOUT THE GAME 📖")
    print("""
Easy Level:
• Select your preferred word set (Animal, Shape, Place)
• 8 lives to guess the secret word

Moderate Level:
• Select your preferred word set (Animal, Shape, Place)
• 6 lives only, making it more challenging

Hard Level:
• Word set is chosen randomly without revealing it
• 6 lives only – guess wisely!

Goal: Guess the secret word with the most lives remaining to top the Hall of Fame!
    """)

def pick_secret_word(level):
    """Selects the secret word based on the chosen level."""
    if level == "Hard":
        selected_set = random.choice(list(WORD_SETS.keys()))
    else:
        print("\nChoose a set of secret words:")
        print("1. Animal\n2. Shape\n3. Place")
        set_choice = get_valid_input("Enter choice (1/2/3): ", ["1", "2", "3"])
        selected_set = list(WORD_SETS.keys())[int(set_choice) - 1]
    return random.choice(WORD_SETS[selected_set]).lower()

# ===============================
# MAIN GAME FUNCTIONALITY
# ===============================
def play_hangman(player_name, level):
    """Core gameplay logic for Hangman."""
    secret_word = pick_secret_word(level)
    guessed_letters = []
    lives = 8 if level == "Easy" else 6

    while lives > 0:
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print(f"\nWord: {display_word}")
        print(f"Lives Remaining: {lives}")

        # Correct index calculation with safeguard
        pic_index = min((8 - lives) if level == "Easy" else (6 - lives), len(HANGMAN_PICS) - 1)
        print(HANGMAN_PICS[pic_index])

        guess = input("Guess a letter: ").lower().strip()
        if not guess.isalpha() or len(guess) != 1:
            print("❌ Please enter a single alphabetical character.")
            continue
        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter.")
            continue

        guessed_letters.append(guess)
        if guess in secret_word:
            print("✅ Correct guess!")
            if all(letter in guessed_letters for letter in secret_word):
                print(f"\n🎉 YOU WIN! The secret word was '{secret_word}'.")
                update_hall_of_fame(level, player_name, lives)
                break
        else:
            print("❌ Incorrect guess.")
            lives -= 1
    else:
        # When lives reach 0, show final state and message
        print(HANGMAN_PICS[-1])
        print(f"\n💀 GAME OVER. You lost! The secret word was '{secret_word}'.")

# ===============================
# MAIN MENU LOOP
# ===============================
def main():
    """Displays the main menu and controls overall game flow."""
    initialize_database()
    player_name = input("Enter your name: ").strip()

    while True:
        print(f"\n👋 Hello, {player_name}!\nWelcome to Advanced Hangman!")
        print("""
1. Play Easy Level
2. Play Moderate Level
3. Play Hard Level
4. View Hall of Fame
5. About the Game
6. Exit
        """)
        menu_choice = get_valid_input("Select an option (1-6): ", ["1", "2", "3", "4", "5", "6"])

        if menu_choice == "1":
            play_hangman(player_name, "Easy")
        elif menu_choice == "2":
            play_hangman(player_name, "Moderate")
        elif menu_choice == "3":
            play_hangman(player_name, "Hard")
        elif menu_choice == "4":
            display_hall_of_fame()
        elif menu_choice == "5":
            show_about_game()
        elif menu_choice == "6":
            print("👋 Goodbye! Thanks for playing Hangman. Have a great day!")
            break

# ===============================
# PROGRAM ENTRY POINT
# ===============================
if __name__ == "__main__":
    main()

