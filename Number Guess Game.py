secret_number = 8

guess = None

print("I'm thinking of a number between 1 and 10. Can you guess it?")

while guess != secret_number:
    try:
        guess = int(input("Enter your guess: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number!")
    except ValueError:
        print("Invalid input. Please enter a whole number.")
