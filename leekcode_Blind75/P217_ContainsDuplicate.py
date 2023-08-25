# Given an integer array nums, return true if any value appears AT LEAST twice
# in the array, and return false, if every element is distinct.

# Example:
#  [1,2,3,1] --> true
#  [1,2,3,4] --> false

class ContainsDuplicate:
   def has_duplicate(self, nums: list[int]) -> bool:
        #Expected Complexity for this function Time - O(n); Space - O(n)
        hashset = set(nums)                 # O(n)
        if len(hashset) == len(nums):       # Len() - O(1) as length is an attribute stored in list and set
            return False
        else:
            return True
