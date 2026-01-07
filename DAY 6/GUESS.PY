secret_number = 7
guess = None

while guess != secret_number:
    guess = int(input("Guess the secret number (between 0 and 10): "))
    if guess >=0 and guess <=10:
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the secret number.")

    
