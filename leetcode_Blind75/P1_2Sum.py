# Given an input array of integers, return indices of the two numbers
# such that they add up to a specific target.

# You must assume that each input would have exactly one solution and
# you may not use the same element twice

# Example: nums = [2, 7, 11, 15] and target = 9
# return [0, 1]

# Logic
    # consider nums = [2, 1, 5, 3]   target = 4
    # Normal approach - start with 2, add 2 to rest of the elements and check the sum
    # Normal approach will give O(n2)
    # Best Approach
        # Start with 2; Subtract from target (4 - 2); can ignore as it is 2
        # go to 1; subtract from target (4 - 1); check if 3 exists

# Data Structure
    # Start creating the HashMap by traversing through List
    # Value: Index pair
    # Add each value to hashMap
    # {"2": 0, "1":1, "5": 2, "3":3}

class TwoSumSolution:
    def twosum(self, nums: list[int], target: int) -> list[int]:
        HashMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in HashMap:
                return [HashMap[diff], i]
            HashMap[n] = i


