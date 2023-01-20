# Import Random module
import random

# Declare and initialize variables
rock = "rock"
scissors = "scissors"
paper = "paper"
game_round = 1
user_points = 0
computer_points = 0
# Declare and initialize list variable that contains options that computer can choose from
choice_list = [rock, paper, scissors]

while True:
    # Save computer's random choice to a variable
    computer_choice = random.choice(choice_list)
    # Request user's input and store it in a variable
    user_choice = input("Enter a choice from one of these: rock, paper, scissors\n")
    print(f"Computer's Chosen Value: {computer_choice}")
    print(f"Your Chosen Value: {user_choice}")

    # First check if the user's choice is a valid one, if not display an error message to them
    if(user_choice not in choice_list) :
        print("You entered a wrong value. Please try again\n")
        continue
    # Check if the user and computer choices are the same
    elif(computer_choice == user_choice) :
        print("You chose the same values\n")
    # Check if computer choice is rock, then play using that scenario
    elif(computer_choice == rock) :
        # If user has chosen scissors, then the computer wins because rock beats scissors
        # else if the user chooses paper, then they win because paper beats rock
        # then the relevant winner's points are increased by 1
        if(user_choice == scissors) :
            print(f"The computer wins game round {game_round}\n")
            computer_points = computer_points + 1
        else :
            print(f"You win game round {game_round}\n")
            user_points = user_points + 1
    elif(computer_choice == scissors) :
        # If user has chosen rock, then the user wins because rock beats scissors
        # else if the user chooses paper, then the computer wins because scissors beats paper
        # then the relevant winner's points are increased by 1
        if(user_choice == rock) :
            print(f"You win game round {game_round}\n")
            user_points = user_points + 1
        else :
            print(f"The computer wins game round {game_round}\n")
            computer_points = computer_points + 1
    elif(computer_choice == paper) :
        # If user has chosen rock, then the computer wins because paper beats rock
        # else if the user chooses scissors, then the user wins because scissors beats paper
        # then the relevant winner's points are increased by 1
         if(user_choice == rock) :
            print(f"The computer wins game round {game_round}\n")
            computer_points = computer_points + 1
         else :
            print(f"You win game round {game_round}\n")
            user_points = user_points + 1

    # Checks to see if the current round is 3 or either of the player's points is 2 already, if so, then the condition is entered to finish the game          
    if(game_round == 3 or user_points == 2 or computer_points == 2) :
        if(user_points == 2) :
            print("You won the game!")
            break
        if(computer_points == 2) :
            print("The computer won the game!")
            break
        if(user_points > computer_points) :
            print("You won the game!")
        elif(user_points < computer_points) :
            print("The computer won the game!")
        else :
            print("You tied the game!")
        break
    # The game round is increased by 1 after a round ends
    game_round = game_round + 1

    
        
