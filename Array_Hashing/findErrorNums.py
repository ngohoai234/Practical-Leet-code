class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0, 0]

        for n in nums:
            n = abs(n)
            nums[n - 1] *= -1
            if nums[n - 1] > 0:
                res[0] = n

        for i, n in enumerate(nums):
            if n > 0 and i + 1 != res[0]:
                res[1] = i + 1
        return res


# 645. Set Mismatch


# You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.
#
# You are given an integer array nums representing the data status of this set after the error.
#
# Find the number that occurs twice and the number that is missing and return them in the form of an array.
#
#
#
# Example 1:
#
# Input: nums = [1,2,2,4]
# Output: [2,3]
# Example 2:
#
# Input: nums = [1,1]
# Output: [1,2]
#
#
# Constraints:
#
# 2 <= nums.length <= 104
# 1 <= nums[i] <= 104


# Solution 1: Sort

# step 1: sort

# step 2: iterate nums
#   step 2.1:

print(Solution.findErrorNums('', [1, 2, 2, 4])
      )
