import random

def select_random_word():
    words = ["python", "hangman", "challenge", "programming", "openai", "university","razak","mental"]
    return random.choice(words)

def display_word_progress(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = select_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print(f"You have {max_incorrect_guesses} incorrect guesses allowed.\n")

    while incorrect_guesses < max_incorrect_guesses:
        print(display_word_progress(word, guessed_letters))
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!\n")
            if all(letter in guessed_letters for letter in word):
                print(f"Congratulations! You've guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess! You have {max_incorrect_guesses - incorrect_guesses} guesses left.\n")

    if incorrect_guesses == max_incorrect_guesses:
        print(f"Sorry, you've run out of guesses. The word was: {word}")

if __name__ == "__main__":
    hangman()
