# RandomizedSet Class
# bool insert(int val) - inserts an item val into the set if not present. Returns true if the item was not present
# bool remove(int val) - Removes an item val from the set if present. Returns true if the item was present.
# int getRandom() - Returns a random element from the current set of elements with the same probability.

# Algorithm
# 1. Use 2 datastructures to store the values HashMap & List/Array
# 2. Insert the value to list and the value+list index to Hash Map
# 3. Removal - Replace the last value in the list with the value to be deleted based on the index.
#            - pop the last value in the list (O(1))
#            - Remove the value in the HashMap
# 5. Random - Get random based on the index values.
import random
class RandomizedSet:
    def __ini__(self):
        self.numMap = {}
        self.numList = []

    def insert(self, val: int) -> bool:
        result = val not in self.numMap         # O(1)
        if result:
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return result

    def remove(self, val: int) -> bool:
        result = val in self.numMap
        if result:
            temp = self.numList[self.numMap[val]]
            self.numList[self.numMap[val]] = self.numList[-1]
            self.numList[-1] = temp
            self.numList.pop()
            del self.numMap[val]
        return

    def getRandom(self) -> int:
        return random.choice(self.numList)
