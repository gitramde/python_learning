# Given an integer array nums, return true if any value appears AT LEAST twice
# in the array, and return false, if every element is distinct.

# Example:
#  [1,2,3,1] --> true
#  [1,2,3,4] --> false

class ContainsDuplicate:
   def has_duplicate(self, nums: list[int]) -> bool:
        hashset = set(nums)
        if len(hashset) == len(nums):
            return False
        else:
            return True
