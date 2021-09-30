import random
import string

def flipCoin():
    return random.choice(["Heads","Tails"])

if __name__ == "__main__":
    print(flipCoin())