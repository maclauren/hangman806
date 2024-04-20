# while loop set to true
while True:
    # ask user to guess letter and assign to guess var
    guess = input("Guess a letter: ")
    # check guess is single alphabetical character using isalpha
    if len(guess) == 1 and guess.isalpha():
        # if guess passes break loop
        break
    # if guess does not pass print message
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")