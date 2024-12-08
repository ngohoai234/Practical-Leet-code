from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            counts = [0] * 26

            for c in s:
                counts[ord(c) - ord('a')] += 1

            res[tuple(counts)].append(s)

        return res.values()

# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]
#
# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


# Example 2:

# Input: strs = ["x"]
#
# Output: [["x"]]

# Example 3:

# Input: strs = [""]
#
# Output: [[""]]


# Solution 1:

# sort all of them
# use hash map to group them

# time: O(n * log(n))

# Solution 2:
# use hash map instead sort
