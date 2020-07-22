from check_words import check_words


def get_words(random_letters, num):
    """
    This function parses words from words.txt (English dictionary) by game's rule.
    (list(str), int) -> (list(str))
    :param random_letters: list of generated letters.
    :param num: amount of generated letters.
    :return: words from English dictionary which contain generated letters and the middle char (necessary).
    """

    f = open('words.txt', 'r')
    result_words = []  # words from dictionary

    with f as en:
        for line in en:
            dict_word = list(line[:-1].lower())  # list of word's letters, -1 because '\n' is in the end
            if check_words(random_letters, dict_word, num):
                result_words.append(line.lower()[:-1])
    return result_words
