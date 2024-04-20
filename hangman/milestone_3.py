# Task 2

# Check if guess is in word
def check_guess(guess, secret_word):
    guess = guess.lower()
    if guess in secret_word:
        # Print message
        print(f"Good guess! '{guess}' is in the word.")
    else:
        # Print message
        print(f"Sorry, '{guess}' is not in the word. Try again.")

# Task 1

# While loop set to True
def ask_for_input(secret_word):
    while True:
        # Ask user to guess letter and assign to guess var
        guess = input("Guess a letter: ")
        # Check if guess is a single alphabetical character using isalpha
        if len(guess) == 1 and guess.isalpha():
            # If guess passes, break loop
            break
        # If guess does not pass, print message
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

    # Call the check_guess function to check if the guess is in the word
    check_guess(guess, secret_word)

secret_word = ""

ask_for_input(secret_word)
