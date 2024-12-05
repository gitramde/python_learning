"""
Pythonic refers to writing code in a way that embraces the principles and idioms of the Python programming language.

In this File we will learn some of the shortcuts Python provides to make our code easy to read and write.

 1. Unpacking - Unpack list, set or tuple into multiple variables
 2. Loop Unpacking - Unpacking to iterate over a list of lists
 3. Enumerate - Access both index and the element while iterating over an array
 4. zip - Iterate over multiple lists at the same time
 5. min max shortcut -  function to ensure a value doesn't exceed a certain limit or exclude negative values
"""

# Unpacking
# If we attempt unpacking with too many variables on the left-side, we will get a ValueError.

point1 = [0, 0]
point2 = [2, 4]

x1, y1 = point1 # This is unpacking
x2, y2 = point2

slope = (y2 - y1) / (x2 - x1)
print(slope)

# Loop Unpacking
points = [[0, 0], [2, 4], [5, 6], [7, 8]]

for x, y in points:
    print(f"x: {x}, y: {y}")

# Enumerate
# Returns a tuple of the index and the element at that index.
# We can unpack this tuple into two variables in the for loop.
nums = [2, 3, 4, 5, 6, 7]
for i, n in enumerate(nums):
    print(i, n)

# Zip
# The zip() function takes multiple lists as arguments and returns an iterator of tuples.
# This is useful when we have multiple lists of the same length and want to iterate over them together.

# Time complexity: O(1)
# The zip() function returns an iterator at the beginning of the input lists, so it doesn't traverse the entire lists.
# Space complexity: O(1)
# The zip() function returns an iterator so it doesn't actually create a new list of tuples in memory.

names = ['Alice', 'Bob', 'Charlie', 'David']
scores = [90, 85, 88, 92]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# convert 2 lists to dictionaries
names = ["Alice", "Bob", "Charlie"]
scores = [90, 80, 70]
name_scores_dict = {}
for name, score in zip(names, scores):
    name_scores_dict[name] = score

# min max shortcut
transactions = 101
transactions = min(100, transactions) # limits the maximum value to 100
transactions = -2
transactions = max(0, transactions) # stop negative values

