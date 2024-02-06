from Module1 import fun as happy
from Module2 import sad as mean
from Module3 import movie as show

import random

def main():
    number = int(input('What is your favorite number?'))



    random_number = random.randint(1, 3)

    if random_number == 1:
        happy.nice_reaction(number)
    elif random_number == 2:
        mean.mean_reaction(number)
    elif random_number == 3:
        show.pick_movie(number)

if __name__ == "__main__":
    main()