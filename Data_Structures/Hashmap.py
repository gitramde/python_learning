"""
In Python, hash maps are implemented using the dict class. The common operations on a hash map include:

All Operations are O(1)

Insertion -
    my_dict = {}
    my_dict['a'] = 1

Deletion -
    del my_dict['a'] # {}
    my_dict.pop('b') # {}
    my_dict.pop('c') # KeyError: 'c'
    my_dict.pop('c', 'default') # No error, returns 'default'

Access -
    my_dict = {'a': 1}
    print(my_dict['a'])

Lookup -
    my_dict = {'a': 1}
    does_a_exist = 'a' in my_dict # True
    does_b_exist = 'b' in my_dict # False
"""

my_dict = {}

my_dict["a"] = 1
my_dict["b"] = 2
my_dict["c"] = 3

my_dict.pop('b') # {}
my_dict.pop('c') # KeyError: 'c'
my_dict.pop('c', 'default') # No error, returns 'default'
print('a' in my_dict) # True
print('b' in my_dict) # False






############################### Challenges ###############################################
"""
Implement the following functions:

build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int].
    It takes two lists, keys and values, and returns a hash map where the keys are the elements of the keys list and
    the values are the elements of the values list.
    This may be a good opportunity to use the zip() function in Python.

get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]. 
    It takes a hash map and a list of keys and returns a list of the values associated with those keys.
    You may assume that all keys in the list exist in the hashmap
    The order of the values in the output list should match the order of the keys in the input list.

"""
from typing import List, Dict


def build_hash_map(keys: List[str], values: List[int]) -> Dict[str, int]:
    my_hash = {}
    for key, value in zip(keys, values):
        my_hash[key] = value
    return my_hash

def get_values(hash_map: Dict[str, int], keys: List[str]) -> List[int]:
    my_list = []
    for key, value in hash_map.items():
        if key in keys:
            my_list.append(hash_map[key])
    return my_list


# do not modify below this line
print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))
print(get_values({"Jane": 25, "Charlie": 60, "Carol": 100, }, ["Jane", "Carol"]))
print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))
