from collections import defaultdict


class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = defaultdict(int)

        res = 0

        for num in nums:
            res += count[num]
            count[num] += 1

        return res


# Given an array of integers nums, return the number of good pairs.
#
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.


# Example 1:
#
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Example 2:
#
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.


# solution 1: for loop


# solution 2:


solution = Solution()

print(solution.numIdenticalPairs([1, 2, 3, 1, 1, 3]
                                 ))
