def check_words(random_letters, dict_word, num):
    """
    The function checks if word from dictionary consists of random letters and
    if a word includes a required letter from the middle of the random letters list.
    (list(str), list(str), int) -> (bool)
    :param random_letters: list of the game's random letters
    :param dict_word: list of dictionary's word letters
    :param num: amount of letters in the param random_letters
    (needed for searching the middle letter of the random_letters)
    :return: True or False
    """

    is_rule = False
    the_same = []
    middle = random_letters[round(num / 2)]  # the middle of random_letters

    for i in dict_word:
        for j in random_letters:
            if i == j:
                the_same.append(j)  # the same letters between random_letters and dict_word
                break

    # if the_same contains 2 equal letters but dict_word no
    if len(dict_word) != len(the_same):
        return is_rule

    for elem in random_letters:

        # if chars in the_same appears more times than in random_letters
        if the_same.count(elem) > random_letters.count(elem):
            is_rule = False
            return is_rule
        else:
            is_rule = True

    if middle not in the_same:
        is_rule = False
        return is_rule

    return is_rule
