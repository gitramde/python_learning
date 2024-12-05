"""
Option 1: sort()
    By default, the .sort() method sorts the elements in ASCENDING order in-place.

    def sort(key=None, reverse=False) -> None:
    The return value of the .sort() method is None.

    This method also works for a list of strings (lexicographical order).

Option 2: sorted()
    The sorted() function returns a new list with the elements sorted in the specified order.
    The original list remains unchanged.

    For the most part, it's similar to the sort() method, but it returns a new list instead of modifying the original list.

"""

# Ascending Order
elements = [5, 3, 6, 2, 1]

elements.sort()

print(elements) # [1, 2, 3, 5, 6]

# Descending Order
elements.sort(reverse=True)

print(elements) # [6, 5, 3, 2, 1]

# Using the "key" parameter to sort based on custom logic

words = ["apple", "banana", "kiwi", "pear", "watermelon", "blueberry", "cherry"]


def get_word_length(word: str) -> int:
    return len(word)

words.sort(key=get_word_length)

#       (Or) Using Lambda

words.sort(key=lambda word: len(word))

print(words)


