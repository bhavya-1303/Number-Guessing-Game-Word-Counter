
import random
import string
from collections import Counter


# -------------------- NUMBER GUESSING GAME --------------------

def play_guessing_game():
    """Play a number guessing game with attempts and scoring."""
    best_score = None

    while True:
        secret_number = random.randint(1, 100)
        max_attempts = 7
        attempts = 0
        score = 0

        print("\n" + "=" * 45)
        print("         NUMBER GUESSING GAME")
        print("=" * 45)
        print("Guess a number between 1 and 100.")
        print(f"You have {max_attempts} attempts.")

        while attempts < max_attempts:
            try:
                guess_text = input(
                    f"\nAttempt {attempts + 1}/{max_attempts} - Enter guess: "
                ).strip()

                guess = int(guess_text)

                if not 1 <= guess <= 100:
                    print("Please enter a number between 1 and 100.")
                    continue

            except ValueError:
                print("Invalid input! Please enter a whole number.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                score = max(0, 100 - (attempts - 1) * 10)
                print(f"\nCorrect! The secret number was {secret_number}.")
                print(f"Attempts used: {attempts}/{max_attempts}")
                print(f"Your score: {score}/100")

                if best_score is None or score > best_score:
                    best_score = score
                    print("New best score!")

                break

        else:
            print("\nGame over! You used all your attempts.")
            print(f"The secret number was {secret_number}.")
            print(f"Attempts used: {attempts}/{max_attempts}")
            print("Your score: 0/100")

        if best_score is not None:
            print(f"Best score this session: {best_score}/100")

        replay = input("\nPlay again? (y/n): ").strip().lower()
        if replay != "y":
            break


# -------------------- WORD COUNTER --------------------

def count_words(path="sample.txt"):
    """Read a text file and return its word-frequency counter."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            text = file.read().lower()

    except FileNotFoundError:
        print(f"\nFile not found: {path}")
        print("Please create the file or check its name and location.")
        return

    # Remove punctuation so words such as 'python!' become 'python'.
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    word_counts = Counter(words)

    print("\n" + "=" * 45)
    print("             WORD COUNTER")
    print("=" * 45)
    print(f"File: {path}")
    print(f"Total words: {len(words)}")
    print(f"Unique words: {len(word_counts)}")

    if not word_counts:
        print("\nThe file is empty or contains no words.")
        return

    print("\nTop 10 most common words:")
    print("-" * 25)
    print(f"{'Word':<15}{'Count':>5}")
    print("-" * 25)

    for word, count in word_counts.most_common(10):
        print(f"{word:<15}{count:>5}")

    print("\nNote: Common words such as 'the', 'is', and 'and'")
    print("can appear frequently in natural language.")


# -------------------- MAIN MENU --------------------

def main():
    """Display the menu and run the selected tool."""
    while True:
        print("\n" + "=" * 45)
        print("     NUMBER GUESSING GAME & WORD COUNTER")
        print("=" * 45)
        print("1. Play Number Guessing Game")
        print("2. Count Words in a Text File")
        print("3. Quit")

        choice = input("\nChoose an option (1-3): ").strip()

        if choice == "1":
            play_guessing_game()
        elif choice == "2":
            path = input(
                "Enter text file name (press Enter for sample.txt): "
            ).strip()
            if not path:
                path = "sample.txt"
            count_words(path)
        elif choice == "3":
            print("\nThank you for using the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
