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


""" 
************* Default Dict ********************

The collections module provides a class called defaultdict that is a subclass of the built-in 
dict class. 
It allows you to set a default value for a key that doesn't exist in the dictionary.

This can be very useful when COUNTING THE FREQUENCY OF ELEMENTS IN A LIST

If a key doesn't exist in the dictionary, it will be created with a default value of the integer 0.
This allows us to increment the value without checking if the key exists.
"""

from collections import defaultdict

nums = [1, 2, 4, 3, 2, 1]
freq = defaultdict(int)

for num in nums:
    freq[num] += 1

print(freq)  # {1: 2, 2: 2, 4: 1, 3: 1}

"""
Counter 

If all we want to do is count the occurrences of elements in a list, 
an even better solution exists than the defaultdict.

We can use the collections.Counter class:
"""

from collections import Counter

nums = [1, 2, 4, 3, 2, 1]

counter = Counter(nums)

print(counter) # Counter({1: 2, 2: 2, 4: 1, 3: 1})

counter[100] += 1 # No error even when the index 100 don't exists

print(counter) # Counter({1: 2, 2: 2, 4: 1, 3: 1, 100: 1})

# to count from multiple lists

nums1 = [1, 2, 4, 3, 2, 1]
nums2 = [1, 2, 3, 4, 5]

print("Counting from multiple lists: ")
counter = Counter(nums1)
counter.update(nums2)

print(counter)  # Counter({1: 3, 2: 3, 4: 2, 3: 2, 5: 1})

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

Implement the following function using a defaultdict:

count_chars(s: str) -> Dict[str, int]
    that takes a string and returns a dictionary where the keys are the characters in the string and 
    the values are the number of times each character appears in the string.
    
        Example: count_chars("hello") should return {'h': 1, 'e': 1, 'l': 2, 'o': 1}

nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]
    that takes a list of lists of integers and returns a dictionary where the keys are the first element
    of each list and the values are the rest of the elements in the list.
    
    Example: The input [[1, 2, 3], [4, 5, 6], [1, 4]] should return {1: [2, 3, 4], 4: [5, 6]}
        You may assume each sublist will have at least two elements.

count_chars(s1: str, s2: str) ->
    CounterType that takes two strings and returns a Counter object
    that counts the occurences of each character in the two strings combined.
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

from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    count = defaultdict(int)

    for char in s:
        count[char] += 1

    return count


def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    output = defaultdict(list)

    for sublist in nums:
        first = sublist[0]

        for i in range(1, len(sublist)):
            output[first].append(sublist[i])

    return output

from collections import Counter
from typing import Counter as CounterType


def count_chars(s1: str, s2: str) -> CounterType:
    counter = Counter(list(s1))
    counter.update(list(s2))
    return counter


# do not modify below this line
print(build_hash_map(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(build_hash_map(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(build_hash_map(["Doug", "Bob", "Tommy"], [80, 90, 100]))

print(get_values({"Alice": 90, "Bob": 80, "Charlie": 70}, ["Alice", "Bob", "Charlie"]))
print(get_values({"Jane": 25, "Charlie": 60, "Carol": 100, }, ["Jane", "Carol"]))
print(get_values({"X": 205, "Y": 78, "Z": 100}, ["Y"]))

print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_toou_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))

print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))

