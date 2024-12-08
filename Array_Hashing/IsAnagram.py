class Solution:

    def char_to_number(self, char: str):
        return ord(char) - ord('a')

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cnt_s = [0] * 26
        cnt_t = [0] * 26

        for i in range(len(s)):
            idx_char_s = self.char_to_number(s[i])
            idx_char_t = self.char_to_number(t[i])

            cnt_s[idx_char_s] = cnt_s[idx_char_s] + 1

            cnt_t[idx_char_t] = cnt_t[idx_char_t] + 1

        return cnt_s == cnt_t


test = Solution()

test.isAnagram("racecar", "carrace")

#
# Is Anagram
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
#
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
#
# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true


# Example 2:
#
# Input: s = "jar", t = "jam"
#
# Output: false


# Constraints:

# s and t consist of lowercase English letters.


# sort s and t

# init i and j = 0

# loop from start to s

#   if s[i] != t[j] -> return False
#   else: i++, j++


# Time: n*Log(n)

# Space: O(1)


# map structure to count
