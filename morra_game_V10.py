import random

#function to validate the user input:
def get_user_number():
    is_number_valid = False
    number = 0
    while (not is_number_valid):
        value = input("\nChoose a number of fingers between (1 and 10): \n")
        try:
            number = int(value)
        except ValueError:
            print("input error: That's not a valid number\n")
        if (number not in range(1, 11)):
            print("input error: You must choose a number between (1 and 10):\n")
        else:
            is_number_valid = True
    return number


def game():
    #begining of each game
    #ask for user input to choose even or odd
    human_choice = input(
        "Which player do you want to be? \n Type in 'evens' or 'odds':\n ")

    while human_choice.lower() not in ("odds", "evens"):
        human_choice = input(
            "input error: make sure to type in 'evens' or 'odds': \n ")

    # set the computer's choice to be the opposite of the input
    if human_choice.lower() == "evens":
        computer_choice = "odds"
    else:
        computer_choice = "evens"
    # display the users and computers choice
    print(
        f"You chose '{human_choice}' so the computer will be '{computer_choice}'\n          Good Luck! ")

    # initializing storing variables:
    human_score = 0
    computer_score = 0
    h_bonus_points = 0
    c_bonus_points = 0
    round_num = 0
    #score history per round:
    round_results = []

    # keep playing rounds while there's no winner (aka one player reaches 6 points):
    while human_score < 6 and computer_score < 6:

        human_fingers = get_user_number()

        # computer's choice of fingers:
        computer_fingers = random.randint(1, 10)
        
        human_score, computer_score, round_num, h_bonus_points, c_bonus_points = game_round(human_choice, human_fingers, computer_fingers, human_score, computer_score, round_num, h_bonus_points, c_bonus_points)
        round_results.append([round_num, human_fingers, human_score, computer_fingers, computer_score])

    print("############## aww! This game is over!#######################")
    print_game_result(human_score, computer_score, round_results, h_bonus_points, c_bonus_points)
    return human_score, computer_score, round_results, h_bonus_points, c_bonus_points


def print_game_result(human_score, computer_score, round_results, h_bonus_points, c_bonus_points):
    # prints the result of a game:
    for i in (round_results):
        print(
            f"Round: {i[0]} | your choice: {i[1]} | your points: {i[2]}| computer choice: {i[3]} |computer points: {i[4]}|")
    print(f"------------------------------------------------------------")
    print(
        f"Final score: your score: {human_score} ({h_bonus_points} bonus pts) ------- computer score: {computer_score} ({c_bonus_points} bonus pts)")
    if human_score == computer_score:
        print("We have a draw!\n")
    elif human_score > computer_score:
        print("You won! :)\n")
    else:
        print("The computer won! :( \n")


def game_round(human_choice, human_fingers, computer_fingers, human_score, computer_score, round_num, h_bonus_points, c_bonus_points):
    # regular points calculation section:
    # find whether the sum is even or odd
    sum_fingers = human_fingers + computer_fingers
    if sum_fingers % 2 == 0:
        if human_choice == "evens":
            winner = "You"
            human_score += 2
        else:
            winner = "Computer"
            computer_score += 2
    else:
        if human_choice == "odds":
            winner = "You"
            human_score += 2
        else:
            winner = "Computer"
            computer_score += 2

    
    # increment round counter:
    round_num += 1

    print(f"####################### ROUND {round_num} #######################")
    # Display the computer's choice, the human choice and the winner of the round
    print(
        f"(Your choice: {human_fingers} + Computer choice: {computer_fingers} = {sum_fingers})")
    print(f" {winner} won this round!")

    # bonus points section:
    if (human_fingers > computer_fingers):
        human_score += 1
        h_bonus_points += 1
        print("-- You got 1 extra point")
    elif (human_fingers < computer_fingers):
        computer_score += 1
        c_bonus_points += 1
        print("-- Computer got 1 extra point")

    # Return the updated scores and the round number:
    return human_score, computer_score, round_num, h_bonus_points, c_bonus_points

#function tokeep playing the game multiple times
def start_games():
    game_rounds = 1
    game_history = []
    keepPlaying = "y"
    # welcome message for game start:
    print("""
 ########################  Welcome to our:  #################################
   
  #     # ####### ######  ######     #        #####     #    #     # ####### 
  ##   ## #     # #     # #     #   # #      #     #   # #   ##   ## #       
  # # # # #     # #     # #     #  #   #     #        #   #  # # # # #       
  #  #  # #     # ######  ######  #     #    #  #### #     # #  #  # #####   
  #     # #     # #   #   #   #   #######    #     # ####### #     # #       
  #     # #     # #    #  #    #  #     #    #     # #     # #     # #       
  #     # ####### #     # #     # #     #     #####  #     # #     # #######
  --------------------------------------------------------------------------
  rules: 
    * Choose between even and odds
    * Choose a number of fingers between 1 and 10
    * If the total is an odd number, odds win and vice versa
    * Winner of each round scores 2 points
    * Who chooses the closest number to the total fingers wins 1 extra point
    * The winner of the game is the first player to reach at least 6 points

 ############################################################################                                                                           
 produced by: Anabela Faria & Ana Ferreira                       EM108__2023
 ----------------------------------------------------------------------------
   """)
    while (keepPlaying == "y"):
        human_score, computer_score, round_results, h_bonus_points, c_bonus_points = game()
        game_history.append([game_rounds, human_score, computer_score, round_results,h_bonus_points, c_bonus_points])
        game_rounds += 1
        keepPlaying = input("Do you want to play again?? y/n > ")
        while (keepPlaying not in ("y", "n")):
            keepPlaying = input("Do you want to play again?? y/n > ")
    print("\n.") 
    #print the history of all games:
    print("***************************** ALL GAMES SCORES:  *********************************")
    print("##################################################################################")
    for g in game_history:
        print(f'Game:{g[0]}--------------')
      
        print_game_result(g[1], g[2], g[3], g[4], g[5])
        print("#############################################################")
    print(f"Total number of games played: {game_rounds-1}")
    
    print("################################################################")
    print("****************************************************************")

start_games()