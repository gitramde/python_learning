# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import heapq
from collections import deque

def variables():
    # Use a breakpoint in the code line below to debug your script.
    n = 0
    while n < 10:
        print(n)
        n += 1

    for i in range(5):
        print(i)

    for i in range(2, 6):
        print(i)

    for i in range(5, 1, -1):
        print(i)

    # Division is decimal by default
    print(5 / 2)
    # double slash rounds down
    print(5 // 2)

    # to round up
    print(int(-3 // 2))

    # use Math for calculations like mod, floor as -10 % 3 will not give right result
    print(math.fmod(-10, 3))
    print(math.floor(3 / 2)) # Round Down
    print(math.ceil(3 / 2)) # Round Up
    print(math.sqrt(2))
    print(math.pow(2, 200))
    print(math.pow(2, 200) < float("inf"))

    # Max/Min Integer
    print(float("inf"))
    print(float("-inf"))

    # Arrays are dynamic by default
    arr = [1, 2, 3]
    print(arr)
    # to add an element
    arr.append(4)
    # to remove an element
    arr.pop(2)
    # to index at a location
    arr.insert(1, 7) # This is O(n) times operation
    print (arr)
    arr[0] = 0 # This is not a O(n) .. it is a constant time operation.

    # Initialize an array of size n with default value of 1
    n = 5
    arr = [1] * n

    print(arr[-1]) # print the last value .. not out of bound errors.
    print(arr[-2]) # print the second last value

    print(arr[1:3]) # slicing an array; from 1 to 2 index

    a, b, c = [1, 2, 3] # unpacking an array

    nums = [1, 2, 3]
    # loop through array
    for i in range(len(nums)):
        print(nums[i])

    for n in nums:
        print(n)

    for i, n in enumerate(nums):
        print (i, n)

    # multiple array simultaneously
    nums1 = [1, 3, 5]
    nums2 = [2, 4, 6]
    for n1, n2 in zip(nums1, nums2):
        print(n1, n2)

    # Reverse an array
    nums1.reverse()
    print(nums1) # This will reverse the array

    # Sorting an array
    nums1.sort()
    print(nums1) # sorted in ascending order
    nums1.sort(reverse=True) # DEscending order
    print(nums1)


    arr_sort = ["bob", "alice", "jane", "doe"]
    arr_sort.sort()
    print(arr_sort) # sorts by alphabetical order
    # sort an array by length of each string
    arr_sort.sort(key=lambda x: len(x))
    print(arr_sort)

    # List Comprehension .. add 0 to 4 to an array
    arr = [i for i in range(5)]
    print(arr)

    # 2D lists
    arr = [[0]*4 for i in range(4)] # Don't use [[0] * 4] * 4
    print(arr)

    # STrings are similar to arrays
    s = "abc"
    print(s[0:2])

    # But they are immutable (We can't modify a string.)
    # s[0] = "A" -- won't work

    # so, this creates a new string
    s += "def"
    print(s)

    # combine a list of strings with deliminter
    strings = ["ab", "cd", "ef"]
    print("".join(strings))

    # Queues (Double ended Queues)
    queue = deque()
    queue.append(1)
    queue.append(2)

    print(queue)

    queue.popleft()
    queue.appendleft(1)

    queue.pop()
    print(queue)

    # Hashset
    mySet = set()

    mySet.add(1)
    mySet.add(2)
    print(mySet)

    print(1 in mySet) # checks if 1 is in the hashset
    print(3 in mySet) # returns false

    mySet.remove(2) # to remove the value 2

    # list to set
    print(set([1, 2, 3]))

    mySet = {i for i in range(5)}
    print(mySet)

    # Hashmap (aka dict)
    myMap = {}
    myMap["alice"] = 88
    myMap["bob"] = 77
    print(myMap)
    print(len(myMap))

    print("alice" in myMap) # check if a key exists
    myMap.pop("alice")      # REmove a key value pair

    myMap = {"alice": 90, "bob": 70}
    print(myMap)

    # Dict Comprehension
    myMap = {i: 2*i for i in range(3) } # creates {0: 0, 1: 2, 2: 4}
    print(myMap)

    # Looping through maps
    myMap = {"alice": 90, "bob": 70}
    for key in myMap:
        print(key, myMap[key])

    for val in myMap.values():
        print(val)

    for key, val in myMap.items():
        print(key, val)

    # Tuples are like arrays but immutable.Can't modify a value
    tup = (1, 2, 3)
    print(tup[1])
    print(tup[2])

    # can be used as a key for hash map/set
    myMap = {(1, 2): 3}
    print(myMap)

    mySet = set()
    mySet.add((1, 2))
    print((1, 2) in mySet)

    # Heaps
    minHeap = []
    heapq.heappush(minHeap, 3)
    heapq.heappush(minHeap, 4)
    heapq.heappush(minHeap, 2)

    # min is always at index 0
    print(minHeap[0])

    while len(minHeap):
        print(heapq.heappop(minHeap))

    # Python don't have max heap by default
    # workaround to multiply by -1 when push & pop
    heapq.heappush(minHeap, -3)
    heapq.heappush(minHeap, -4)
    heapq.heappush(minHeap, -2)

    # Build heap from initial values
    arr = [2, 1, 8, 4, 5]
    heapq.heapify(arr)
    while arr:
        print(heapq.heappop(arr))

    # min is always at index 0
    print(-1 * minHeap[0])

# Nested functions
def outer(a, b):
    c = 0

    def inner():
        return a+b+c
    return inner()

class MyClass:
    # constructor
    def __init__(self, nums):
        #create member variables
        self.nums = nums
        self.size = len(nums)

    def getLength(self):
        return self.size

    def getDoubeLength(self):
        return 2 * self.getLength()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    variables()
    print(outer(1, 2))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
