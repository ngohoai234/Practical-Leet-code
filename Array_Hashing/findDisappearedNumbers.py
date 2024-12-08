class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for i in range(len(nums)):
            curr_num = abs(nums[i])
            if nums[curr_num - 1] > 0:
                nums[curr_num - 1] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res


# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.


# Example 1:
#
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]


# Example 2:
#
# Input: nums = [1,1]
# Output: [2]

# Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.


# solution 1:
# create an array for count
# iterate num in nums
#   assign count[num] += 1
# ...

solution = Solution()

print(solution.findDisappearedNumbers([1, 1]))

# 4 3 2 7 8 2 3 1
# |
# 4 3 2 -7
