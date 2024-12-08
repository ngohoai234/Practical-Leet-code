from collections import defaultdict


class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        map_ps = defaultdict(str)
        map_sp = defaultdict(str)

        splited = s.split(' ')

        if len(pattern) != len(splited):
            return False

        for i in range(len(splited)):
            p = pattern[i]
            c = splited[i]
            if (p in map_ps and map_ps[p] != c) or (c in map_sp and map_sp[c] != p):
                return False
            map_ps[p] = c
            map_sp[c] = p

        return True


# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:
#
# Each letter in pattern maps to exactly one unique word in s.
# Each unique word in s maps to exactly one letter in pattern.
# No two letters map to the same word, and no two words map to the same letter.
#
# Example 1:
#
# Input: pattern = "abba", s = "dog cat cat dog"
#
# Output: true
#
# Explanation:
#
# The bijection can be established as:
#
# 'a' maps to "dog".
# 'b' maps to "cat".
# Example 2:
#
# Input: pattern = "abba", s = "dog cat cat fish"
#
# Output: false
#
# Example 3:
#
# Input: pattern = "aaaa", s = "dog cat cat dog"
#
# Output: false


solution = Solution()

print(solution.wordPattern('aaaa', 'dog cat cat dog'))
