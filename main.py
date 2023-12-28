from getpass import getpass
from words import word_gm1
import random

print("Do you want to play: \n")
game_mode = int(input("1) One player\n2) Two players\n"))

if game_mode == 1:
    position = random.randint(0, len(word_gm1))
    word = word_gm1[position]
   
else:
    word = getpass("Write a word for player 2 to guess: ")

user_letters = []
chances = 7

print("======================")


while True:
    for letter in word:
        if letter.lower() in user_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")

    print(f"\n\nYou have {chances} chances")

    attempt = input("Choose a letter: ")
    user_letters.append(attempt.lower())
    if attempt.lower() not in word.lower():
        chances -= 1

    win = True
    for letter in word:
        if letter.lower() not in user_letters:
            win = False

    if chances == 0 or win:
        break


if win:
    print(f"Congrats!! you won the game. The word was: {word}")
else:
    print(f"You lost the game, the word was: {word}")
