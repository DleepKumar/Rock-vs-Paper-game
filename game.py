import random

def print_rules():
    print("Winning Rules of the Rock Paper Scissors game:")
    print("Rock vs paper -> paper wins")
    print("Rock vs scissor -> Rock wins")
    print("Paper vs scissor -> scissor wins")

def get_choice_name(choice):
    if choice == 1:
        return 'Rock'
    elif choice == 2:
        return 'Paper'
    elif choice == 3:
        return 'Scissors'

def game():
    print_rules()
    
    while True:
        # Ask user for their choice
        user_choice = int(input("\nEnter your choice: 1 for Rock, 2 for Paper, 3 for Scissors: "))
        
        # Check if the user input is valid
        if user_choice not in [1, 2, 3]:
            print("Invalid choice, please enter 1, 2, or 3.")
            continue
        
        user_choice_name = get_choice_name(user_choice)
        print(f"\nYour choice is: {user_choice_name}")
        
        # Get the computer's choice using random number generator
        comp_choice = random.randint(1, 3)
        comp_choice_name = get_choice_name(comp_choice)
        print(f"Computer's choice is: {comp_choice_name}")
        
        # Determine the winner
        if user_choice == comp_choice:
            print("It's a tie!")
        elif (user_choice == 1 and comp_choice == 2) or \
             (user_choice == 2 and comp_choice == 3) or \
             (user_choice == 3 and comp_choice == 1):
            print("Computer wins!")
        else:
            print("You win!")
        
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
game()
