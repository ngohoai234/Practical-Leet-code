class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0

        for i in range(len(s)):
            ch = s[i]

            if i % 2 == 0:
                if ch == '0':
                    res += 1
            else:
                if ch == '1':
                    res += 1

        return min(res, len(s) - res)


# 1758. Minimum Changes To Make Alternating Binary String

# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.
#
# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.
#
# Return the minimum number of operations needed to make s alternating.

solution = Solution.minOperations('', '110010')

print(solution)
