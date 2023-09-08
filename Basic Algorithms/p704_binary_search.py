# Given a sorted (ascending order) array of integers (nums)
# and an integer target
# write a function to search target in nums.

# Assumptions - All integers in the nums are unique.

# If target exists, then return its index. Otherwise return -1
# runtime complexity must be O(log n)

# NOTE:
# check the mid point and search left or right based on the value.
# Loop will run the number of times you can divide the length of array by 2.
# 16 -> 8 -> 4 -> 2 -> 1
# log2(n)
from typing import List

def binary_search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums)-1

    while l <= r:
        # mid = l + r // 2  --- If the array is huge it may through integer exception
        mid = l + ((r - l)//2)
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    print(binary_search([-1, 0, 3, 5, 9, 12], 15)) # Output -1
    print(binary_search([-1, 0, 3, 5, 9, 12], 5))  # Output 3