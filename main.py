from string import ascii_lowercase
from generate_grid import generate_grid
from get_words import get_words


def get_pure_user_words(num=9):
    """
    Main process of the game run.
    This function gets words from user, checks them, counts wrong and right inputs (in points).
    (int) -> None
    :param num: amount of the letters to construct words from. (Default is 9).
    :returns None.
    """

    while True:
        random_letters = generate_grid(num)  # letters for user to create words
        words_from_dict = get_words(random_letters, num)  # all words from a dictionary that consist generated letters
        if len(words_from_dict) > num:
            break


    print('Set up the words using these letters: ', random_letters, '\nYour word must contain',
          random_letters[round(num / 2)], 'letters.\nWords should not be repeated. Good luck! :)')

    counter = 0
    well = 0
    wrong = 0

    # The main process of the game
    while counter < num:

        try:
            user_word = input('Enter a word, please: ')

            if all(i not in ascii_lowercase for i in user_word):
                raise ValueError

            if user_word in words_from_dict:
                words_from_dict.remove(user_word)
                print('You are right! :)')
                well += 1

            else:
                print('You are wrong! :(')

        except ValueError:
            print('Only letters!')
            wrong += 1

        finally:
            counter += 1

    print('Your result:', well, 'from', num)


if __name__ == '__main__':
    get_pure_user_words()
