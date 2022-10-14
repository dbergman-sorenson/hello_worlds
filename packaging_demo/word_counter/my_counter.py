from collections import Counter


def count_in_list(mylist: list, word: str):
    # count instances of word in mylist
    c = Counter(mylist)
    return c[word]
