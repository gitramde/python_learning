############################################ LISTS ##################################################
"""
Lists
    - Collection of items stored in a specific order.
    - Some languages have both fixed-size arrays and resizable arrays.
      In Python, we only have resizable arrays, which are referred to as lists in Python.
    - Lists are MUTABLE (element value can be changed)
    - Common Operations
        - append() -> [O(1)] Add an element at the end of the list
        - pop() -> [O(1)] Removes and return the last element of the list
            1. If the list is already empty, we will get an IndexError.
            2. We can also pop a specific index. If we pop(index) an index that is out of bounds,
               we will get an IndexError.
        - insert() -> [O(1)] Inserts an element at a specified index in the list.
        - index()  -> [O(n)] Returns the index of the first occurrence of a specified element in the list.
        - remove() -> [O(n)] Removes the first occurrence of a specified element from the list.
        - extend() -> [O(n)] Add elements of another list to the end of the list
"""
# Easiest way to create an empty list of specific size in python

my_list = [0] * 5 # Creates a list of 5 zeroes

# List comprehension
print("start: List Comprehension")
my_list = [i for i in range(5)]

print(my_list) # [0, 1, 2, 3, 4]

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
result = [i+j for i, j in zip(arr1, arr2)] # [1, 2, 3, 4, 5, 6]

arr = [1, 2, 3, 4, 5]

result = [i for i in arr if i % 2 == 0] # [2, 4]

print("end: List Comprehension")
my_list = [1, 2, 3, 4]
# check if list is empty
if my_list:
    print("List is not empty")

# Check if an element is present in the list

if 2 in my_list:
    print("Available in the list ")

# Return the index of a list element
print(my_list.index(3))

# Access leftmost and rightmost element
print(my_list)
print(f" Left most element - [0]: {my_list[0]}")
print(f" Right most element - [-1]: {my_list[-1]}")

# Looping through List
print("start: looping through the list")
for i in range(len(my_list)):
    print(my_list[i])

for element in my_list:
    print(element)
print("end: looping through the list")

# Aggregation of List

print(sum(my_list))
print(max(my_list))
print(min(my_list))

# Methods to alter the list ( Methods are associated to an object)
# Append method .. Appends a new value to the end of the list
print(f"List :{my_list}")
my_list.append(5)
print(f"After appending 5 to the end: {my_list}")


# Pop Method .. Removes the last element of the list by default
# but can delete the element at any index as well.
#    - This method also returns the popped out value.
#
my_list.pop()
print(f"After popping the last value: {my_list}")
pop_output = my_list.pop(0) # Removes the first element from the list and returns that element
print(f"Popped value: {pop_output}")
print(f"After popping the first value: {my_list}")

# Insert elements into the list
my_list.insert(0,1)
print(f"After insertion: {my_list}")

my_list = [1, 3, 2, 3]

print(f"New List for next 3 operations: {my_list}")

element = my_list.index(3) # 1

print(f"element at the index 3: {element}")

my_list.remove(3) # [1, 2, 3]

print(f"After removing the first occurence of element 3: {my_list}")

my_list.extend([4, 5]) # [1, 2, 3, 4, 5] Time Complexity - O(m)

# Other way to concatenate the lists - This creates a new list ...
# extend() modifies the original list

result = my_list + [4, 5] # O(n+m)

print(f"After extending the list by another list: {my_list}")

# List Slicing
"""
Slicing →
 my_list[start:end:step] 
        1. Does not include the character at the index end 
        2. If Step is omitted, it is defaulted to 1 

 Examples:
    my_list[:3] → First 3 elements of the list
    my_list[4:] → From 4th elements till end of the list
    my_list[-2:] → Last 2 elements of a list
    my_list[::-1] → Reverse a list 

"""

print("*************** Slicing ******************")
print(f"Original List - {my_list}")
print(f"First 3 elements of the list - {my_list[:3]}")
print(f"From 4th elements to end of list - {my_list[4:]}")
print(f"Last 2 elements of the list - {my_list[-2:]}")
print(f"Reverse a list - {my_list[::-1]}")

# Cloning a list
"""
Python provides multiple ways to clone a list. Here are a few ways to do it:
1. Using the copy() method
2. Using the slicing syntax
3. using the list() constructor 
4. Using copy.deepcopy() for deep copies (Nested objects in list ... like list of lists)
"""
original_list = [1, 2, 3]
cloned_list = original_list.copy()

cloned_list = original_list[:]

cloned_list = list(original_list)

import copy

original_list = [[1, 2], [3, 4]]

cloned_list = copy.deepcopy(original_list)




############################################ Tuples ##################################################

""" 
Tuples are very similar to lists, but they have one key difference: they are immutable.

We can create a tuple by using parentheses... my_tuple = (4, 5, 6)

    1. pop() and append() doesn't work .
    2. sum(), max() and min() works on tuples
    3. Slicing a tuple doesn't modify it, instead it creates a new tuple with the specified slice.

"""

############################################ SETS ##################################################
"""
In Python, a set is very similar to a list, but with a few key differences.

    1. A set is unordered, meaning the elements are not stored in a specific order. 
       If order is important, you should use a list.
    2. A set can only contain unique elements. If you try to add a duplicate element to a set, it will be ignored.
    
"""

my_set = {1, 2, 3}

my_set = set()
# If we used empty curly braces {}, it would not have declared a set.
# That's because Python uses curly braces to declare an empty dictionary.
my_set.add(1)
my_set.add(2)

# convert list to set
my_set = set(my_list)

# Set Operations
#   Remove() - to remove an element
my_set.remove(2) # If the element doesn't exists, it raises KeyError

# Looping through sets
# Just like with lists, we can loop over elements within a set using for loops.
# The difference is that we can't access elements by index because sets are unordered.
# The order that we loop over a set is not guaranteed.

my_set = {1, 2, 3}

for element in my_set:
    print(element)

contains_1 = 1 in my_set

############################################ DICTIONARY ##################################################

"""
Used to store key-value pairs. The simplest way of thinking about them is as a table with two columns.
The first column is the key, and the second column is the value.

we are mapping a key to the value. 
This is why dictionaries are sometimes called maps or hashmaps in other programming languages.

    1. Dictionaries can't have duplicate keys
    2. Like Set we can't loop through with the length of the dictionary 
    3. 
"""

my_dict = {}

my_dict["Alice"] = 25
my_dict["Bob"] = 30
my_dict["Charlie"] = 35

# To check if a key exists in the dictionary
print("Alice" in my_dict)

# Looping through dictionary
for key in my_dict:
    print(key, my_dict[key])

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)

 # Remove the key "Alice".
# IF the second parameter is "0" then it won't raise keyerror for key that doesn't exists.

my_dict.pop("Ram", 0)

# Implement the above using exception handling
# Throws KeyError .. If any other exception, just show the value
try:
    my_dict.pop("Ram")
except KeyError:
    print("Error: KeyError value!")
except Exception as error:
    print("Error: ", error)

# one Usage of dictionary - count number of occurences of a character in string
word = "hello"
char_count = {}
for char in word:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)

