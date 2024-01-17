# Prompts

## Prompt 1
    Create a class in python called GameLogic. This class will have two static methods. The first method is called "calculate_score" and the second method is called "roll_dice".

## Response 1

    import random

    class GameLogic:
        @staticmethod
        def calculate_score(dice_values):
            """
            Calculate the score based on the given dice values.

            Parameters:
            - dice_values (list): A list of integers representing the values of rolled dice.

            Returns:
            - int: The calculated score.
            """
            # Your scoring logic here
            score = sum(dice_values)  # Example: Sum of all dice values
            return score

        @staticmethod
        def roll_dice(num_dice):
            """
            Simulate rolling a specified number of dice.

            Parameters:
            - num_dice (int): The number of dice to roll.

            Returns:
            - list: A list of random integers representing the values of rolled dice.
            """
            # Your dice rolling logic here
            dice_values = [random.randint(1, 6) for _ in range(num_dice)]  # Example: Rolling a six-sided die
            return dice_values

    # Example usage:
        dice_values = GameLogic.roll_dice(3)
        score = GameLogic.calculate_score(dice_values)
        print(f"Dice values: {dice_values}")
        print(f"Calculated score: {score}")

## Prompt 2
    Make a roll dice method that takes in an integer in-between 1-6, based off the amount of the integer return a random number in a tuple. python

## Response 2
    import random

    def roll_dice(dice_value):
        if 1 <= dice_value <= 6:
            # Generate random numbers based on the dice value
            result = tuple(random.randint(1, 6) for _ in range(dice_value))
            return result
        else:
            print("Invalid dice value. Please choose a value between 1 and 6.")

    # Example usage:
        dice_value = 3  # You can replace this with any integer between 1 and 6
        result_tuple = roll_dice(dice_value)
        print(f"Rolling {dice_value} dice: {result_tuple}")


## Prompt 3

    I attemted to prompt for the calculated_score method but I wasn't able to get chatGPT to respond with a viable answer. After, writing my own code, I accidentally deleted the prompts for the 3rd part of this lab. Sorry!





