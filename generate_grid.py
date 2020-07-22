from random import choice
from string import ascii_lowercase


def generate_grid(num):
    """
    The function generates randomized list of letters for game.
    (int) -> (list(str))
    :param num: amount of the letters to generate for game.
    :return: list of the random chars
    """

    random_letters = [choice(ascii_lowercase) for _ in range(num)]
    for index in random_letters:
        if random_letters.count(index) > 2:  # letters shouldn't be repeated more than 2 times
            generate_grid(num)

    return random_letters
