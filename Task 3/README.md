# Hangman Game

This repository contains a Python console-based Guess The Word (Hangman) game where one player thinks of a word and the other player tries to guess it letter by letter. The guessing player has a limited number of incorrect guesses before they lose. The game displays the progress of the guessed word, the remaining attempts, and a visual representation of the Hangman.

## Features

- Random word selection from a predefined list of words.
- Displays the progress of the guessed word with blanks for unguessed letters.
- Shows the remaining incorrect guesses allowed.
- Visual representation of the Hangman as incorrect guesses are made.
- Handles invalid inputs (non-alphabetic characters, multiple characters, previously guessed letters).
- Allows players to play multiple rounds.

## How to Play

1. The game randomly selects a word from the list.
2. The player guesses letters one by one.
3. Correct guesses reveal the positions of the letters in the word.
4. Incorrect guesses reduce the number of remaining attempts and add to the Hangman drawing.
5. The game ends when the player either guesses the word correctly or runs out of attempts.

## How to Run

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/hangman-game.git
    cd hangman-game
    ```

2. **Run the Game**:
    ```sh
    python hangman.py
    ```

3. **Follow the On-Screen Prompts**: The game will guide you through the process of guessing the word, showing the Hangman drawing, and handling your inputs.

## Example

```plaintext
H A N G M A N
------
 |    |
      |
      |
      |
      |
=========
Missed letters: 
_ _ _ _ _

Guess a letter: a
------
 |    |
 O    |
      |
      |
      |
=========
Missed letters: a
_ _ _ _ _

Guess a letter: e
------
 |    |
 O    |
      |
      |
      |
=========
Missed letters: a e
_ _ _ _ _

Guess a letter: o
------
 |    |
 O    |
      |
      |
      |
=========
Missed letters: a e
_ o _ _ _

Guess a letter: p
------
 |    |
 O    |
 |    |
      |
      |
=========
Missed letters: a e p
_ o _ _ _

Guess a letter: n
------
 |    |
 O    |
 |    |
/     |
      |
=========
Missed letters: a e p n
_ o _ _ _

Guess a letter: l
------
 |    |
 O    |
 |    |
/ \   |
      |
=========
Missed letters: a e p n l
_ o _ _ _

Guess a letter: g
------
 |    |
 O    |
/|\   |
/ \   |
      |
=========
Missed letters: a e p n l g
_ o _ _ _

Guess a letter: y
------
 |    |
 O    |
/|\   |
/ \   |
      |
=========
Missed letters: a e p n l g y
_ o _ _ _

Guess a letter: r
------
 |    |
 O    |
/|\   |
/ \   |
      |
=========
Missed letters: a e p n l g y r
_ o r _ _

Guess a letter: d
Yes! The secret word is 'word'! You have won!
Do you want to play again? (yes/no): no
Thanks for playing!
