"""
Python does not have a built-in sorted dictionary data structure. 

sorted containers is a third-party library that provides a SortedDict class, 
which maintains the keys in sorted order.

https://grantjenks.com/docs/sortedcontainers/

"""
# Insert the values into the sorted dictionary

from sortedcontainers import SortedDict

sorted_dict = SortedDict()

sorted_dict['C'] = 90

sorted_dict['B'] = 80

sorted_dict['A'] = 70

print(sorted_dict)  # SortedDict({'A': 70, 'B': 80, 'C': 90})

# Accessing the values associated with the keys

sorted_dict = SortedDict({'a': 1})

print(sorted_dict['a']) # 1

""" Deletion: Delete a key-value pair from the sorted dict.
There are several ways to delete a key-value pair from a sorted dictionary.
  popitem() method to remove and return the first or last key-value pair in sorted order.
    - will raise a KeyError if the dictionary is empty.
  pop() method to remove and return the value associated with a specific key, or the del keyword to delete a key-value pair.
    - will raise a KeyError if the key does not exist.
The del keyword will also raise a KeyError if the key does not exist.
"""
sorted_dict = SortedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

# removes & return the last key-value pair in sorted order
sorted_dict.popitem() # ('d', 4)

# removes & return the first key-value pair in sorted order
sorted_dict.popitem(0) # ('a', 1) 

# remove & return the value associated with the key
sorted_dict.pop('b') # 2

del sorted_dict['c'] # {}

# Lookup: Check if a key exists in the sorted dict.

sorted_dict = SortedDict({'a': 1})

does_a_exist = 'a' in sorted_dict # True
does_b_exist = 'b' in sorted_dict # False

# Iterating through a sorted dict 

sorted_dict = SortedDict({'a': 1, 'b': 2, 'c': 3})

for key, value in sorted_dict.items():
    print(key, value)