import random
from time import sleep

import src.helpers


def choose_house():
    """
    Choose House method picks the Hogwarts House that you should be placed in.
    :return: None
    """
    chosen_house = random.choice(['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin'])
    song = """\nThere's nothing hidden in your head\nThe Sorting Hat can't see,\nSo try me on and I will tell you\nWhere you ought to be."""
    print(song)
    sleep_timer = random.randint(1, 4)
    sleep(sleep_timer)
    house = f"The house of which you belong is {chosen_house}!"
    src.helpers.print_random_cowsay_way(house)

