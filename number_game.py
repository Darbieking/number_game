# Import the random module for generating random numbers
import random

# Get the upper limit of the range for the random number from user input
top_of_range = input("Type a number: ")

# Check if the input is a digit
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    # Check if the number is greater than zero
    if top_of_range <= 0:
        print("Type a number larger than zero, Omoko!!")
        quit()
else:
    print("Type in a number....Buko")
    quit()

# Generate a random number within the specified range
random_number = random.randint(0, top_of_range)

# Initialize a variable to count the number of guesses
number_of_guesses = 0

# Start a loop for the user to make guesses
while True:
    # Increment the number of guesses
    number_of_guesses += 1

    # Get user input for a guess
    user_guess = input("Guess a number: ")

    # Check if the input is a digit
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Type in a number....Buko")
        continue

    # Check if the guess is correct
    if user_guess == random_number:
        print("You got it right")
        break
    # Provide feedback on the guess
    elif user_guess > random_number:
        print("Your guess is greater than the number!!")
    else:
        print("Your guess is below the number!!")

# Display the number of guesses it took to get the correct answer
print(f"You got it in {number_of_guesses} guesses")
