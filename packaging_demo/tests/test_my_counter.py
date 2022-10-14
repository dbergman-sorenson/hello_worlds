from unittest import TestCase, main
from packaging_demo.word_counter.my_counter import count_in_list


class Test(TestCase):
    def test_count_in_list(self):
        mylist = ['hi', 'hello', 'hey', 'hello', 'w', 'hey', 'hello']
        myset = set(mylist)
        print(f"Word list is {mylist}:")
        for word in myset:
            mycount = count_in_list(mylist=mylist, word=word)
            print(f"I counted {mycount} instances of {word}.")
            if word == 'hi':
                self.assertEqual(mycount, 1)
            elif word == 'hello':
                self.assertEqual(mycount, 3)
            elif word == 'hey':
                self.assertEqual(mycount, 2)
            elif word == 'w':
                self.assertEqual(mycount, 1)

if __name__ == '__main__':
    main()