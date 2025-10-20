"""
Sorted sets are very similar to hash sets, but they store keys in sorted order.
Sorted sets may not contain duplicate elements. The common operations on a sorted set include:

Insertion: Insert a key into the sorted set.

Deletion: Delete a key from the sorted set.

Lookup: Check if a key exists in the sorted set.

Iterating: Loop through the sorted set.

"""

# Insertion: Insert the values into the sorted set

from sortedcontainers import SortedSet

my_set = SortedSet()

my_set.add(90)
my_set.add(80)
my_set.add(85)

print(my_set) # SortedSet([80, 85, 90])

# Deletion: Delete a key from the sorted set.

"""
The remove() method will raise a KeyError if the element does not exist, while the discard() method will not.
The pop() method will remove and return the largest element in the sorted set.
The pop(0) method will remove and return the smallest element in the sorted set.
The clear() method will remove all elements from the sorted set.
"""

my_set = SortedSet([90, 80, 85, 95])

my_set.remove(90) # SortedSet([80, 85, 95])

my_set.discard(100) # SortedSet([80, 85, 95]) 

my_set.pop() # 95

my_set.pop(0) # 80

print(my_set) # SortedSet([85])

my_set.clear() # SortedSet([])

# Lookup: Check if a key exists in the sorted set.

my_set = SortedSet([80, 85, 90])

does_a_exist = 'a' in my_set # True
does_b_exist = 'b' in my_set # False

# Iterating: Loop through the sorted set.

sorted_set = SortedSet([4, 3, 5, 2, 1])

for num in sorted_set:
    print(num)  # 1, 2, 3, 4, 5

