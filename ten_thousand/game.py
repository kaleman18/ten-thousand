from game_logic import GameLogic
from collections import Counter

round_tracker = 1
dice_remaining = 6
total_score = 0
unbanked_points = 0
previous_score = 0
response_checker = 0
response = ""
dice_checker = None


def start():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    response = input("> ")

    if response == "y":
        roll_dice_start()

    if response == "n":
        print("Okay! Maybe another time.")
        return

def reroll():
     
    global dice_remaining
    global unbanked_points
    global total_score
    global round_tracker
    global response
    global dice_checker

    print(f"Rolling {dice_remaining} dice...")

    dice_checker = GameLogic.roll_dice(dice_remaining)
    
    check_for_cheater_and_roll_dice()

def roll_dice_start():
    global dice_remaining
    global unbanked_points
    global total_score
    global round_tracker
    global previous_score
    global response
    global dice_checker

    print(f"Starting round {round_tracker}")

    print(f"Rolling {dice_remaining} dice...")

    dice_checker = GameLogic.roll_dice(dice_remaining)

    check_for_cheater_and_roll_dice()

def roll_dice():
    global dice_remaining
    global unbanked_points
    global total_score
    global round_tracker
    global previous_score
    global response
    global dice_checker

    print(f"You banked {previous_score} points in round {round_tracker}")

    previous_score = 0

    print(f"Total score is {total_score} points")

    round_tracker += 1

    print(f"Starting round {round_tracker}")

    print(f"Rolling {dice_remaining} dice...")

    dice_checker = GameLogic.roll_dice(dice_remaining)

    check_for_cheater_and_roll_dice()

def check_for_cheater_and_roll_dice():

    global dice_remaining
    global unbanked_points
    global total_score
    global round_tracker
    global previous_score
    global response
    global dice_checker

    print("*** ", dice_checker," ***")

    if GameLogic.calculate_score(dice_checker) == 0:
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")
        dice_remaining = 6
        unbanked_points = 0
        roll_dice()

    print("Enter dice to keep, or (q)uit:")
    response == ""
    response = input("> ")
    if response == "q":
        print(f"Thanks for playing. You earned {total_score} points")
        return
    response = list(response)
    response = [int(i) for i in response]

    #anti cheat
    if len(response) > dice_remaining:
        print("Cheater!!! Or possibly made a typo...")
        check_for_cheater_and_roll_dice()
        
    dice_rolled_dict = Counter(dice_checker)

    for num in response:
        if num not in dice_rolled_dict :
            print("Cheater!!! Or possibly made a typo...")
            check_for_cheater_and_roll_dice()

        if num in dice_rolled_dict:
            dice_rolled_dict[num] -= 1

        if num in dice_rolled_dict and dice_rolled_dict[num] == -1:
            print("Cheater!!! Or possibly made a typo...") 
            check_for_cheater_and_roll_dice()

    if len(response) == 6:
        unbanked_points += GameLogic.calculate_score(response)
        print(f"You have {unbanked_points} unbanked points and {dice_remaining} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        response == ""
        response = input("> ")
        
        if response == "r":
            reroll()

        if response == "b":
            dice_remaining = 6
            total_score += unbanked_points
            previous_score += unbanked_points
            unbanked_points = 0
            roll_dice()

        if response == "q":
             print(f"Thanks for playing. You earned {total_score} points")
             return
        
        check_for_cheater_and_roll_dice()

    
    else:
        
        dice_remaining = dice_remaining - len(response)
        unbanked_points += GameLogic.calculate_score(response)
        print(f"You have {unbanked_points} unbanked points and {dice_remaining} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        response == ""
        response = input("> ")
        
        if response == "r":
            reroll()

        if response == "b":
            dice_remaining = 6
            total_score += unbanked_points
            previous_score += unbanked_points
            unbanked_points = 0
            roll_dice()

        if response == "q":
             print(f"Thanks for playing. You earned {total_score} points")
             return


if __name__ == "__main__":
    start()

