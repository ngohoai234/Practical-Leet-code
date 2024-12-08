class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = None
        c = 0
        for num in nums:
            if c == 0:
                res = num
            if res == num:
                c += 1
            else:
                c -= 1
        return res


# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.z

# Example 1:
#
# Input: nums = [3,2,3]
# Output: 3
#
# Example 2:
#
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

# initlize {}
# iterate of array nums
# step 1:

#   {
#       3: 1
#   }

# step 2:

# {
#       2 : 1
# }


# Time: O(n)
# Space: O(n)


# Solution 2:

# c = 0
# 3,2,3
# |
# res = 3


# c = 0
# 3,2,3
#   |
# res = 3


