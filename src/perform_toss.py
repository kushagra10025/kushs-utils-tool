import random
import src.helpers

def flipCoin():
	ch = random.choice(["Heads","Tails"])
	print("The values for Coin Toss is :")
	result = "{ %s }" % ch
	src.helpers.print_random_cowsay_way(result)
