import random

print()
print("-----------------------------------")
print("WElCOME TO THE NUMBER GUESSING GAME")
print("-----------------------------------")
print()
print("I'm thinking of a number between 1 and 100. \n"
      "You have 5 chances to guess the correct number.\n")


# DIFFICULTY MODE
def set_difficulty():
    while True:
        level = input("Set a difficulty: \n"
        "[1] EASY 10 chances \n"
        "[2] MEDIUM 5 chances \n"
        "[3] HARD 3 chances \n"
        "Enter the number: ")

        if level in ["1", "2", "3"]:
            level= int(level)
            break
        else:
            print("Invalid Input")    

    if level == 1:
        print("You have selected the EASY level")
        return 10
    elif level == 2:
        print("You have selected the MEDIUM level")
        return 5
    elif level == 3:
        print("You have selected the HARD Level")
        return 3


# GAME STARTING POINT
def game_start(chances):

    num_to_guess = random.randint(1, 100)
    chances_used = 0

    while chances_used < chances:

        remaining = chances - chances_used

        print(f"You have {remaining} chances left.")

        player = input("Enter your guess: ")
        
        if not player.isdigit():
            print("Invalid Input: Input must be numbers only.")
            continue
        
        player = int(player)
        chances_used += 1

        if player == num_to_guess:
            print(f"Congratulations!! You guessed the correct number in {chances_used} attempts! ")
            return True
        elif player > num_to_guess:
            print("Your number guess is too high.")
        else:
            print("Your number guess is too low.")

    print(f"You ran out of chances! The correct number is {num_to_guess}")
    return False


# RESTARTING GAME
def restart():
    
    while True:
        play_again = input("Play again: Y/N: ").lower().lstrip()

        if play_again == "y":
            return True
        elif play_again == "n":
            return False
        else:
            print("Invalid Input: input must be y/n only.")

def main():

    try_again = True

    while try_again:
        
        chances = set_difficulty()
        game_start(chances)
        try_again = restart()
    print("Nice game! Thanks for playing.")

if __name__ == "__main__":
    main()

        







