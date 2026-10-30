import random

WORDS = ['python', 'java', 'javascript', 'php']

def play_game():
    target_word = random.choice(WORDS)
    guessed_letters = set()
    attempts_left = 8

    while attempts_left > 0:
        display_word = "".join([char if char in guessed_letters else "-" for char in target_word])
        print()
        print(display_word)

        if "-" not in display_word:
            print(f"You guessed the word {target_word}!")
            print("You survived!")
            return

        user_input = input("Input a letter: > ")

        if len(user_input) != 1:
            print("You should input a single letter")
            continue

        if not (user_input.isascii() and user_input.islower() and user_input.isalpha()):
            print("Please enter a lowercase English letter")
            continue

        if user_input in guessed_letters:
            print("You've already guessed this letter")
            continue

        guessed_letters.add(user_input)

        if user_input not in target_word:
            print("That letter doesn't appear in the word")
            attempts_left -= 1

    print("You lost!")

def main():
    print("HANGMAN")
    while True:
        choice = input('Type "play" to play the game, "exit" to quit: > ')
        if choice == "play":
            play_game()
        elif choice == "exit":
            break

if __name__ == "__main__":
    main()git add hangman.py