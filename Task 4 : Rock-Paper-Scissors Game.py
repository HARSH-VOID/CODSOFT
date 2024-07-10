import random

def get_user_choice():
    choices = ["rock", "paper", "scissors"]
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(result)

def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, result)
    return result

def play_game():
    user_score = 0
    computer_score = 0
    rounds_played = 0
    
    print("Welcome to Rock, Paper, Scissors!\n")
    
    while True:
        result = play_round()
        rounds_played += 1
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"\nScores after {rounds_played} rounds:")
        print(f"User: {user_score}")
        print(f"Computer: {computer_score}")
        
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\nThanks for playing!")
    print(f"Final Scores: User: {user_score}, Computer: {computer_score}")

if __name__ == "__main__":
    play_game()
