import copy
from collections import Counter, defaultdict


class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        counter = Counter(chars)
        res = 0
        for word in words:
            dict_word = defaultdict(int)
            is_match = True
            for ch in word:
                dict_word[ch] += 1
                if ch not in counter or dict_word[ch] > counter[ch]:
                    is_match = False
                    break

            if is_match == True:
                res += len(word)

        return res


# 1160. Find Words That Can Be Formed by Characters
# You are given an array of strings words and a string chars.
#
# A string is good if it can be formed by characters from chars (each character can only be used once).
#
# Return the sum of lengths of all good strings in words.

# Example 1:
#
# Input: words = ["cat","bt","hat","tree"], chars = "atach"
# Output: 6
# Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

# Example 2:
#
# Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# Output: 10
# Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


# solution 1: hash table

# use hash to count character

# iterate through words
#   if ch in chars
#       subtract the count in variable counter
#

solution = Solution().countCharacters

print(solution(["hello", "world", "leetcode"], 'welldonehoneyr'))
