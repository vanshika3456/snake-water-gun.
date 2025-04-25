
import random

def get_computer_choice():
    choices = ["snake", "water", "gun"]
    return random.choice(choices)

def get_user_choice():
    while True:
        choice = input("\nEnter your choice (snake/water/gun): ").lower()
        if choice in ["snake", "water", "gun"]:
            return choice
        print("Invalid choice! Please try again.")

def get_result(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "snake" and computer_choice == "water":
        return "You win! Snake drinks water"
    elif user_choice == "water" and computer_choice == "gun":
        return "You win! Water drowns gun"
    elif user_choice == "gun" and computer_choice == "snake":
        return "You win! Gun shoots snake"
    else:
        return "Computer wins!"

def play_game():
    print("WELCOME TO THE GAME OF SNAKE WATER GUN:")
    print("FOLLOW THE RULES:")
    print("1. SNAKE DRINKS WATER")
    print("2. WATER DROWNS GUNS")
    print("3. GUN SHOOTS SNAKE")
    print("4. IF BOTH ARE SAME THEN IT IS TIE")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        result = get_result(user_choice, computer_choice)
        print(f"\nResult: {result}")
        
        play_again = input("\nWant to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\nThanks for playing!")

if __name__ == "__main__":
    play_game()
