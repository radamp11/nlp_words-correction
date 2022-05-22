from utils import levenshtein_distance


def print_levensthein(tok1, tok2):
    print(levenshtein_distance(tok1, tok2))


if __name__ == '__main__':
    print_levensthein('jacek', 'placek')
