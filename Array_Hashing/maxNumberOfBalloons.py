from collections import Counter


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counter = Counter(text)
        return int(min(counter.get('b', 0), counter.get('a', 0), counter.get('l', 0) / 2, counter.get('o', 0) / 2,
                       counter.get('n', 0)))

        # given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.
        #
        # You can use each character in text at most once. Return the maximum number of instances that can be formed.

        # Example 1:
        #
        #
        #
        # Input: text = "nlaebolko"
        # Output: 1
        # Example 2:
        #
        #
        #
        # Input: text = "loonbalxballpoon"
        # Output: 2
        # Example 3:
        #
        # Input: text = "leetcode"
        # Output: 0

        # solution 1:

        # iterate text and count frequently characters

        # iterate array count
        #   iterate text balloon


solution = Solution()
print(solution.maxNumberOfBalloons('nlaebolko'))
