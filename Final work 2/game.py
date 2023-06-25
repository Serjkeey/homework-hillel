import random

def game_rules(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "rock" and (computer_choice == "scissors" or computer_choice == "lizard")) or \
         (player_choice == "scissors" and (computer_choice == "paper" or computer_choice == "lizard")) or \
         (player_choice == "paper" and (computer_choice == "rock" or computer_choice == "spock")) or \
         (player_choice == "lizard" and (computer_choice == "spock" or computer_choice == "paper")) or \
         (player_choice == "spock" and (computer_choice == "rock" or computer_choice == "scissors")):
        return "Player"
    else:
        return "Computer"

def play_again():
    while True:
        choice = input("Repeat (Y/N)? ").strip().lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Invalid input. Please enter Y or N.")

def main():
    choices = ["rock", "paper", "scissors", "lizard", "spock"]
    play = True

    print("Game: Rock, Paper, Scissors, Lizard, Spock")

    while play:
        player_choice = input("Your choice (rock, paper, scissors, lizard, spock)? \n>>>").strip().lower()

        if player_choice in choices:
            computer_choice = random.choice(choices)
            print("Player:", player_choice)
            print("Computer:", computer_choice)

            winner = game_rules(player_choice, computer_choice)

            if winner == "Player":
                print("Player WIN!")
            elif winner == "Computer":
                print("Computer WIN!")
            else:
                print("It's a Tie!")

            play = play_again()
        else:
            print("Invalid input.")

    print("Thank you for playing!")

if __name__ == "__main__":
    main()
