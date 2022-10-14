# Python packaging demo
# Reference: https://www.geeksforgeeks.org/how-to-build-a-python-package/

import collections


def count_in_list(mylist: list, word: str):
    # count instances of word in mylist
    c = collections.Counter(mylist)
    return c[word]
