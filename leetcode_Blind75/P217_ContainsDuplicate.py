# Given an integer array nums, return true if any value appears AT LEAST twice
# in the array, and return false, if every element is distinct.

# Example:
#  [1,2,3,1] --> true
#  [1,2,3,4] --> false


class ContainsDuplicate:
    def has_duplicate(self, nums):
        # Expected Complexity for this function Time - O(n); Space - O(n)
        hashset = set(nums)  # O(n)
        if len(hashset) == len(
            nums
        ):  # Len() - O(1) as length is an attribute stored in list and set
            return False
        else:
            return True

    def has_duplicate_sol2(self, nums):
        # Expected complexity for this function: Time - O(n log n); Space - O(1)
        nums.sort()  # Python sorting algorithm - O(n logn) for average and worst; O(n) for best
        print(type(nums))
        for i, n in enumerate(nums):
            if (
                i != len(nums) - 1 and n == nums[i + 1]
            ):  # First condition avoids list index out of range error
                return True
        return False


if __name__ == "__main__":
    cd = ContainsDuplicate()
    print(cd.has_duplicate_sol2([1, 2, 3, 4]))
