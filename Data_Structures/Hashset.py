"""
Hash sets are very similar to hash maps, but they ONLY STORE KEYS without any associated values.
Hash sets also CANNOT CONTAIN DUPLICATES, just like hash maps.
In Python, hash sets are implemented using the set class. The common operations on a hash set include:
"""

# INSERTION:  O(1)
my_set = set()
my_set.add('a') # {'a'}

# DELETION:  O(1)
#  remove() method to delete an element from a hash set. If the element does not exist, the method will raise a KeyError.
#  discard() method, which will not raise an error if the element does not exist.
my_set = {'a'}

my_set.remove('a') # {}
my_set.remove('a') # KeyError

my_set.add('b') # {'b'}
my_set.discard('b') # {}
my_set.discard('b') # {} (no error)

# LOOKUP:  O(1)

my_set = {'a'}

'a' in my_set # True
'b' in my_set # False

"""
Implement the following functions:

build_hash_set(keys: List[str]) -> Set[str]. 
  It takes a list of strings and returns a hash set containing those strings.
  
check_keys(hash_set: Set[str], keys: List[str]) -> List[bool]. 
  It takes a hash set and a list of keys and returns a list of booleans indicating whether each 
  key exists in the hash set. The order of the booleans in the output list should match the order 
  of the keys in the input list.

     Example: check_keys({'a', 'b', 'c'}, ['a', 'd', 'c']) should return [True, False, True].
"""
def build_hash_set(keys: List[str]) -> Set[str]:
    my_set = set()
    for key in keys:
        my_set.add(key)
    return my_set


def check_keys(hash_set: Set[str], keys: List[str]) -> List[bool]:
    output = []
    for key in keys:
        output.append(key in hash_set)
    return output

