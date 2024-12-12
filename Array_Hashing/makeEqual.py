from collections import defaultdict


class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        counter = defaultdict(int)

        for word in words:
            for ch in word:
                counter[ch] += 1

        for c in counter:
            if counter[c] % len(words):
                return False

        return True

# 1897. Redistribute Characters to Make All Strings Equal

# You are given an array of strings words (0-indexed).
#
# In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from words[i] to any position in words[j].
#

# Return true if you can make every string in words equal using any number of operations, and false otherwise.
