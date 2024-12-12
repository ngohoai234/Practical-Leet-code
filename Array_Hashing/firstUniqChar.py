from collections import Counter


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = Counter(s)

        for i, ch in enumerate(s):
            if counter[ch] == 1:
                return i
        return -1


print(Solution.firstUniqChar('', ''))


# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:
#
# Input: s = "leetcode"
#
# Output: 0
#
# Explanation:
#
# The character 'l' at index 0 is the first character that does not occur at any other index.
#
# Example 2:
#
# Input: s = "loveleetcode"
#
# Output: 2
#
# Example 3:
#
# Input: s = "aabb"
#
# Output: -1
#
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists of only lowercase English letters.