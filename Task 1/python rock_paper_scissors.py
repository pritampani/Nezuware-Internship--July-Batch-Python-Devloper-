import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

def main():
    print("Welcome to Rock, Paper, Scissors Game!")
    player_score = 0
    computer_score = 0

    while True:
        player_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        
        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)

        if winner == "tie":
            print("It's a tie!")
        elif winner == "player":
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score - You: {player_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing! Final score - You: {}, Computer: {}".format(player_score, computer_score))

if __name__ == "__main__":
    main()
