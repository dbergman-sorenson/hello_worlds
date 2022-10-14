from packaging_demo import count_in_list

mylist=['hi', 'hello', 'hey', 'hello', 'w', 'hey', 'hello']
myset = set(mylist)
print(f"Word list is {mylist}:")
for word in myset:
    mycount = count_in_list(mylist=mylist, word=word)
    print(f"I counted {mycount} instances of {word}.")
