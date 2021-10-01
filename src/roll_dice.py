import random
import src.helpers

def random_dice_roll(min = 1, max = 6):
	a = random.randint(min, max)
	b = random.randint(min, max)
	print("The values for Dices Roll are : ")
	result = "{ %s , %s }" % (a,b)
	src.helpers.print_random_cowsay_way(result)
