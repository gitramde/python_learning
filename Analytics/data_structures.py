############################################ LISTS ##################################################
"""
Lists
    - Collection of items stored in a specific order.
    - Lists are MUTABLE (element value can be changed)
"""

my_list = [1, 2, 3, 4]
# check if list is empty
if my_list:
    print("List is not empty")

# Check if an element is present in the list

if 2 in my_list:
    print("Available in the list ")

# Return the index of a list element
print(my_list.index(3))

# Looping through List
for i in range(len(my_list)):
    print(my_list[i])

for element in my_list:
    print(element)

# Aggregation of List

print(sum(my_list))
print(max(my_list))
print(min(my_list))

# Methods to alter the list ( Methods are associated to an object)
# Append method .. Appends a new value to the end of the list
print(my_list)
my_list.append(5)
print(my_list)

# Pop Method .. Removes the last element of the list by default
# but can delete the element at any index as well.
my_list.pop()
print(my_list)
my_list.pop(0) # Removes the first element of the list
print(my_list)

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

############################################ LISTS ##################################################

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

