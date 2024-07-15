import random

HANGMAN_PICS = [
    """
     ------
     |    |
          |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
          |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    =========
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    =========
    """
]

WORDS = [
    "python", "java", "kotlin", "javascript", "typescript", 
    "swift", "hangman", "programming", "developer", "algorithm"
]

def get_random_word():
    return random.choice(WORDS)

def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMAN_PICS[len(missed_letters)])
    print("\nMissed letters:", " ".join(missed_letters))

    blanks = "_" * len(secret_word)
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    print(" ".join(blanks))

def get_guess(already_guessed):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Try again.")
        elif not guess.isalpha():
            print("Please enter a letter.")
        else:
            return guess

def play_again():
    return input("Do you want to play again? (yes/no): ").lower().startswith("y")

def main():
    print("H A N G M A N")

    missed_letters = ""
    correct_letters = ""
    secret_word = get_random_word()
    game_done = False

    while True:
        display_board(missed_letters, correct_letters, secret_word)

        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters += guess

            found_all_letters = True
            for i in range(len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                print(f"Yes! The secret word is '{secret_word}'! You have won!")
                game_done = True
        else:
            missed_letters += guess
            if len(missed_letters) == len(HANGMAN_PICS) - 1:
                display_board(missed_letters, correct_letters, secret_word)
                print(f"You have run out of guesses!\nAfter {str(len(missed_letters))} missed guesses and {str(len(correct_letters))} correct guesses, the word was '{secret_word}'")
                game_done = True

        if game_done:
            if play_again():
                missed_letters = ""
                correct_letters = ""
                game_done = False
                secret_word = get_random_word()
            else:
                print("Thanks for playing")
                break

if __name__ == "__main__":
    main()
