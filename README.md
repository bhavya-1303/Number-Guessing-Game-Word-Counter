# Number Guessing Game & Word Counter

## Project Overview
This project is a Python command-line application that combines a number guessing game with a text-file word counter.

## Features
- Generates a random number between 1 and 100.
- Allows up to 7 valid guessing attempts.
- Provides "Too high" and "Too low" hints.
- Calculates the player's score and tracks the best score during the session.
- Validates user input to prevent crashes from invalid guesses.
- Reads text files safely using UTF-8 encoding.
- Counts words without distinguishing uppercase and lowercase.
- Removes punctuation before counting words.
- Displays total words, unique words, and the top 10 most frequent words.
- Handles missing files with a friendly message.
- Provides a menu to switch between the game and word counter.

## Scoring Rule
The player has 7 valid attempts to guess a number between 1 and 100.

- Correct first guess: 100 points.
- Each additional incorrect valid guess reduces the potential score by 10 points.
- Correct guesses on later attempts receive a lower score.
- Failure to guess within 7 attempts: 0 points.
- Invalid inputs and out-of-range numbers do not consume attempts.

## Technologies Used
- Python 3.10 or newer
- `random`
- `string`
- `collections.Counter`
- Visual Studio Code
- Git and GitHub

## Project Files
- `main.py` — Contains the guessing game, word counter, and main menu.
- `sample.txt` — Sample text used to test word frequency analysis.
- `README.md` — Project documentation.

## How to Run
1. Install Python 3.10 or newer.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Ensure `main.py` and `sample.txt` are in the same folder.
5. Run the following command:

   ```bash
   python main.py
   ```

6. Choose an option from the menu:
   - `1` — Play Number Guessing Game
   - `2` — Count Words in a Text File
   - `3` — Quit

## Word Counter Output
The word counter reports the total number of words, the number of unique words, and the ten most frequent words. Common words may appear frequently because they are used often in natural language.

## Testing
The program can be tested with:
- Valid and invalid guesses.
- Guesses outside the range of 1 to 100.
- Winning and losing a game.
- Replaying the game.
- A normal text file.
- A missing text file.
- An empty text file.

## Author
Bhavya
