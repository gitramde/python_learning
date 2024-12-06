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