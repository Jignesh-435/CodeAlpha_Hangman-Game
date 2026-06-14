import random

def play_hangman():
    # 1. Setup the game parameters
    word_list = ["python", "coding", "intern", "script", "github"]
    secret_word = random.choice(word_list)
    guessed_letters = []
    incorrect_guesses_left = 6

    print("Welcome to CodeAlpha Hangman!")
    print("Try to guess the secret word. You have 6 incorrect guesses allowed.")
    
    # 2. Main game loop
    while incorrect_guesses_left > 0:
        print("\n" + "-"*30)
        
        # Display the current state of the word
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print(f"Word: {display_word.strip()}")
        print(f"Incorrect guesses remaining: {incorrect_guesses_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Check if the user has guessed the entire word
        # (If there are no underscores left in the display, they won!)
        if "_" not in display_word:
            print(f"\n🎉 Congratulations! You guessed the word: '{secret_word}'!")
            break

        # 3. Get user input
        guess = input("Guess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input! Please enter a single alphabetical letter.")
            continue
        
        if guess in guessed_letters:
            print(f"⚠️ You already guessed the letter '{guess}'. Try a different one.")
            continue

        # Add the guess to our tracked list
        guessed_letters.append(guess)

        # 4. Check if the guess is correct
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            incorrect_guesses_left -= 1

    # 5. Game Over check
    if incorrect_guesses_left == 0:
        print("\n" + "="*30)
        print("💥 Game Over! You ran out of guesses.")
        print(f"The secret word was: '{secret_word}'")
        print("="*30)

# Run the game
if __name__ == "__main__":
    play_hangman()
