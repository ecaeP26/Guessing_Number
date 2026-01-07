
# DIFFICULTY MODE OPTIONS
def set_difficulty():

    while True:
        try:
            difficulty = int(input("Choose difficulty: [1] Easy [2] Medium [3] Hard: "))    

            if difficulty in (1, 2 ,3):
                break
            else:
                print("Choose the numbers only from 1-3.")
        except ValueError:
            print("Input Invalid. Type a number.")
    
    if difficulty == 1:
        print("You selected the Easy Mode. You have 10 attempts to guess the number from 1-100")
        return 10
    if difficulty == 2:
        print("You selected the Medium Mode. You have 7 attempts to guess the number from 1-100")
        return 7
    else:
        print("You selected the Hard Mode. You have 5 attempts to guess the number from 1-100")
        return 5
# GAME START
def game_start(chances):
    
    attempts = 0
    num_guess = random.randint(1, 100)

    while attempts < chances:

        remaining = chances - attempts

        try:
            print(f"{remaining} chances remaining.")
            player = int(input("Enter your guess number: "))

            if not (1 <= player <= 100):
                print("Enter a number from 1-100 only.")
                continue

        except ValueError:
            print("Input Invalid. Alphabetical and sysmbols are not allowed.")
            continue

        attempts += 1

        if player == num_guess:
            print(f"Congratulations!! You've guessed the correct number in {attempts} attempts!!")
            return True
        elif player < num_guess:
            print("Too low")
        else:
            print("Too high")

    print(f"You've run out of chances! Better Luck next time :(")
    return False
# GAME RESTART
def game_reset():
    
    while True:
        try_again = input("Would you like to play again? [Y/N]: ").lower()

        if try_again not in ("y", "n"):
            print("Enter [Y] Yes or [N] No only.")
        elif try_again == "y":
            return True
        else:
            return False 

def main():

    game_restart = True

    while game_restart:
        chances = set_difficulty()
        game_start(chances)
        game_restart = game_reset()
    print("Thanks for playing!!")

if __name__ == "__main__":
    main()