class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        res = -1
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] and num[i] == num[i + 2]:
                res = max(res, int(num[i]))

        return '' if res == -1 else str(res) * 3

# 2264. Largest 3-Same-Digit Number in String


# You are given a string num representing a large integer. An integer is good if it meets the following conditions:
#
# It is a substring of num with length 3.
# It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.
#
# Note:
#
# A substring is a contiguous sequence of characters within a string.
# There may be leading zeroes in num or a good integer.

# Example 1:
#
# Input: num = "6777133339"
# Output: "777"
# Explanation: There are two distinct good integers: "777" and "333".
# "777" is the largest, so we return "777".
# Example 2:
#
# Input: num = "2300019"
# Output: "000"
# Explanation: "000" is the only good integer.
# Example 3:
#
# Input: num = "42352338"
# Output: ""
# Explanation: No substring of length 3 consists of only one unique digit. Therefore, there are no good integers.

solution = Solution

print(solution.largestGoodInteger(solution, '6777133339'))
