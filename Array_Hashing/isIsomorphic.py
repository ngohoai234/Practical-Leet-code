from collections import defaultdict


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_st = defaultdict(str)
        map_ts = defaultdict(str)
        for i in range(len(s)):
            s1 = s[i]
            t1 = t[i]
            if (s1 in map_st and map_st[s1] != t1) or (t1 in map_ts and map_ts[t1] != s1):
                return False

            map_st[s1] = t1
            map_ts[t1] = s1
        return True


# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itsel

# Example 1:


# Input: s = "badc", t = "baba"

# Output: true
#

# loop in s

#  if s != t
#


solution = Solution()

print(solution.isIsomorphic('paper', 'title'))
