# Make a programme for guessing the number

expected_number = 21
number_of_guesses = 1
print("Guess number game\nNumber is guesses is limited to only 7 times")

while number_of_guesses <= 7:
    guessed_number = int(input("\nGuess the number(number should be between 1 and 100) :\n"))
    if guessed_number < expected_number:
        print("You have guessed a number less than expected number")
    elif guessed_number > expected_number:
        print("You have guessed a number greater than the expected number")
    else:
        print("Bravo!!!, Perfect Guess...")
        print("No. of guesses you took to finish :", number_of_guesses)
        break
    print(7 - number_of_guesses, "guesses left...")
    number_of_guesses += 1
if number_of_guesses > 7:
    print("Game over!!!")
