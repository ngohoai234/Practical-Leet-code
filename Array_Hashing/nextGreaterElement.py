class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        map = {}
        stack = []
        res = []

        for num in nums2:
            while len(stack) and stack[len(stack) - 1] < num:
                map[stack.pop()] = num
            stack.append(num)

        for num in nums1:
            if num in map:
                res.append(map.get(num))
            else:
                res.append(-1)

        return res

# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.
#
# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.
#
# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.
#
# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

# Example 1:
#
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
# Output: [-1,3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
# - 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
# - 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.

# Example 2:Follow up: Could you find an O(nums1.length + nums2.length) solution?
#
# Input: nums1 = [2,4], nums2 = [1,2,3,4]
# Output: [3,-1]
# Explanation: The next greater element for each value of nums1 is as follows:
# - 2 is underlined in nums2 = [1,2,3,4]. The next greater element is 3.
# - 4 is underlined in nums2 = [1,2,3,4]. There is no next greater element, so the answer is -1.

# Follow up: Could you find an O(nums1.length + nums2.length) solution?


# s = [1]

# iterate from 1 to n

#   while s.top() < nums[i]
#       s.pop()
