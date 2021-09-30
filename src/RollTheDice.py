import random

def random_dice_roll(min = 1, max = 6):
    
    print("Rolling the dices...")
    print("The values are....")
    print(random.randint(min, max))
    print(random.randint(min, max))

if __name__ == "__main__":
    random_dice_roll()