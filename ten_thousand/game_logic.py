import random


class GameLogic:

    def calculate_score(dice_values):

        total_score = 0

        three_pairs = 0

        # checking for 1,2,3,4,5,6
        if dice_values.count(1) == 1 and dice_values.count(2) == 1 and dice_values.count(3) == 1 and dice_values.count(4) == 1 and dice_values.count(5) == 1 and dice_values.count(6) == 1:
            
            total_score += 1500

        # checking for an amount of one number, if so assign the correct value to the amount of that one number.
        elif dice_values:

            if dice_values.count(1):

                count_of_ones = dice_values.count(1)

                if count_of_ones == 1:
                    total_score += 100

                if count_of_ones == 2:
                    three_pairs += 1
                    total_score += 200

                if count_of_ones == 3:
                    total_score += 1000

                if count_of_ones == 4:
                    total_score += 2000
                
                if count_of_ones == 5:
                    total_score += 3000
                
                if count_of_ones == 6:
                    total_score += 4000

            if dice_values.count(2):

                count_of_ones = dice_values.count(2)

                if count_of_ones == 2:
                    three_pairs += 1

                if count_of_ones == 3:
                    total_score += 200

                if count_of_ones == 4:
                    total_score += 400
                
                if count_of_ones == 5:
                    total_score += 600
                
                if count_of_ones == 6:
                    total_score += 800

            if dice_values.count(3):

                count_of_ones = dice_values.count(3)

                if count_of_ones == 2:
                    three_pairs += 1

                if count_of_ones == 3:
                    total_score += 300

                if count_of_ones == 4:
                    total_score += 600
                
                if count_of_ones == 5:
                    total_score += 900
                
                if count_of_ones == 6:
                    total_score += 1200

            if dice_values.count(4):

                count_of_ones = dice_values.count(4)

                if count_of_ones == 2:
                    three_pairs += 1

                if count_of_ones == 3:
                    total_score += 400

                if count_of_ones == 4:
                    total_score += 800
                
                if count_of_ones == 5:
                    total_score += 1200
                
                if count_of_ones == 6:
                    total_score += 1600

            if dice_values.count(5):

                count_of_fives = dice_values.count(5)

                if count_of_fives == 1:
                    total_score += 50

                if count_of_fives == 2:
                    three_pairs += 1
                    total_score += 100

                if count_of_fives == 3:
                    total_score += 500

                if count_of_fives == 4:
                    total_score += 1000

                if count_of_fives == 5:
                    total_score += 1500
                
                if count_of_fives == 6:
                    total_score += 2000

            if dice_values.count(6):

                count_of_ones = dice_values.count(6)

                if count_of_ones == 2:
                    three_pairs += 1

                if count_of_ones == 3:
                    total_score += 600

                if count_of_ones == 4:
                    total_score += 1200
                
                if count_of_ones == 5:
                    total_score += 1800
                
                if count_of_ones == 6:
                    total_score += 2400

            # checking for three pairs
            if three_pairs == 3:
                total_score += 1500

        return total_score


    def roll_dice(num_dice):
        if 1 <= num_dice <= 6:
            # Generate random numbers based on the dice value and making it a tuple
            result = tuple(random.randint(1, 6) for _ in range(num_dice))
            return result




