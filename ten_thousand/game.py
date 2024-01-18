from game_logic import GameLogic

round_tracker = 1
dice_remaining = 6
total_score = 0
unbanked_points = 0
previous_score = 0

def play():
    start()


def start():
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    response = input("> ")

    if response == "y":
        roll_dice()

    if response == "n":
        print("Okay! Maybe another time.")
        return

def reroll():
     
    global dice_remaining
    global unbanked_points
    global total_score
    global round_tracker

    print(f"Rolling {dice_remaining} dice...")

    GameLogic.roll_dice(dice_remaining)
    print(f"Current Unbanked Points = {unbanked_points}")
    print(f"Total Score = {total_score}")
    print("Enter dice to keep, or (q)uit:")

    response = input("> ")

    if response == "q":
        print(f"Thanks for playing. You earned {total_score} points")

    else:
        saved_dice = list(response)
        saved_dice = [int(i) for i in saved_dice]
        dice_remaining = dice_remaining - len(saved_dice)
        unbanked_points += GameLogic.calculate_score(saved_dice)
        print(f"You have {unbanked_points} unbanked points and {dice_remaining} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        response = input("> ")
        
        if response == "r":
            reroll()
        if response == "b":
            dice_remaining = 6
            total_score += unbanked_points
            unbanked_points = 0
            round_tracker += 1
            roll_dice()
        if response == "q":
             print(f"Thanks for playing. You earned {total_score} points")
             return

def roll_dice():

    global dice_remaining
    global unbanked_points
    global total_score
    global round_tracker
    global previous_score
    print(f"You banked {previous_score} points in round {round_tracker - 1}")

    previous_score = 0

    print(f"Starting round {round_tracker}")

    print(f"Total Score = {total_score}")

    print(f"Rolling {dice_remaining} dice...")

    GameLogic.roll_dice(dice_remaining)

    print("Enter dice to keep, or (q)uit:")

    response = input("> ")

    if response == "q":
        print(f"Thanks for playing. You earned {total_score} points")

    else:
        saved_dice = list(response)
        saved_dice = [int(i) for i in saved_dice]
        dice_remaining = dice_remaining - len(saved_dice)
        unbanked_points += GameLogic.calculate_score(saved_dice)
        print(f"You have {unbanked_points} unbanked points and {dice_remaining} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        response = input("> ")
        
        if response == "r":
            reroll()
        if response == "b":
            dice_remaining = 6
            total_score += unbanked_points
            previous_score += unbanked_points
            unbanked_points = 0
            round_tracker += 1
            roll_dice()

        if response == "q":
             print(f"Thanks for playing. You earned {total_score} points")
             return


        



        




    
    
if __name__ == "__main__":
    play()


