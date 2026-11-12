# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a command-line Hangman game to practice Python strings, lists, loops, conditionals, random selection, and user input.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Choose a secret word from the provided list and prepare the game state so the player can track their progress.

#### Requirements
Completed program should:

- Randomly select one word from the provided `words` list.
- Track the letters the player has guessed.
- Set and track the maximum number of incorrect guesses allowed.
- Show the secret word as underscores, with correctly guessed letters revealed.

### 🛠️ Play and Finish the Game

#### Description
Let the player guess letters until they reveal the word or run out of incorrect guesses.

#### Requirements
Completed program should:

- Ask the player for a letter and compare it with the secret word.
- Reveal matching letters and keep track of incorrect guesses.
- Display the current word progress and remaining incorrect guesses after each turn.
- End when the player guesses the word or reaches the incorrect-guess limit.
- Display a clear win or loss message; on a loss, reveal the secret word.
