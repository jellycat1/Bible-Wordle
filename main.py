import random
import time

with open('bible_words.txt', 'r') as f:
    file = f.read()
    f.close()
words_list = file.split("\n")

# Define ANSI escape codes for text and background colors
class TextColor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    GRAY = '\033[90m'
    RESET = '\033[0m'

class BackgroundColor:
    BLACK = '\033[40m'
    RED = '\033[41m'
    GREEN = '\033[42m'
    YELLOW = '\033[43m'
    BLUE = '\033[44m'
    MAGENTA = '\033[45m'
    CYAN = '\033[46m'
    WHITE = '\033[47m'
    GRAY = '\033[100m'
    RESET = '\033[0m'

def color_word(goal_word, player_word):
    return ["green" if player_word[i] == goal_word[i] else "yellow" if player_word[i] in goal_word else "gray" for i in range(5)]


# goal_word = "HELLO"

# Rules
rules = """
All words will be in uppercase.
You will get six tries to guess a randomly picked word.
All words are from the Bible.
When you input a word, you will get your word colored.
If the background color of a letter in your word is gray, the letter is not in the word.
If the background color of a letter in your word is yellow, the letter is somewhere else in the word.
If the background color of a letter in your word i green, the letter is in the right place.
Every word is five letters long.
Enter q or quit to end the game.
Good luck!
"""
# Welcome player
print("Welcome to Bible Wordle!")
# Asks if the player knows the rules
knows_rules = input("Do you know the rules? (y/n): ")
# Checks if the player knows the rules
# If the player doesn't know the rules, print out the rules
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
if knows_rules.lower() == "n":
    print(rules)
while True:
    goal_word = random.choice(words_list)
    tries = 0
    while True:
        tries += 1
        if tries == 7:
            print(f"Oh no, you lost! You have already used all six tries... :( The word was {goal_word}")
            break
        print("\nLet's play!")
        while True:
            word = input("Enter a word (uppercase): ")
            if len(word) != 5:
                print("Your word was not five letters long! Please enter a word five letters long.")
                continue
                
            if word != word.upper():
                print("Your word was not all uppercase. Please enter an ALL-UPPERCASE word.")
                continue
            
            contains = False
            for i in word:
                if not i in alphabet:
                    contains = True
            if contains:
                print("Your word containes symbols and/or numbers and/or spaces. Please enter word with five letters.")
                continue

            if word.lower() == "q" or word.lower() == "quit":
                print("Okay, thanks for playing!")
                quit()
            break

        colors_list = color_word(goal_word, word)

        for i in range(5):
            if colors_list[i] == "green":
                print(f"{BackgroundColor.GREEN}{word[i]}{BackgroundColor.RESET} ", end="")
            elif colors_list[i] == "yellow":
                print(f"{BackgroundColor.YELLOW}{word[i]}{BackgroundColor.RESET} ", end="")
            else:
                print(f"{BackgroundColor.GRAY}{word[i]}{BackgroundColor.RESET} ", end="")

        if all(color == "green" for color in colors_list):
            print(f"Yay! You guessed the word in {tries} tries! You won!")
            break
    user_input = input("Do you want to play again (y/n)?\n")
    if user_input == "n":
        print("Ok! Bye!")
        break