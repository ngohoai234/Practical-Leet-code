class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        f = [0] + flowerbed + [0]
        c = 0
        for i in range(1, len(f) - 1, 1):
            flower = f[i]
            prev = f[i - 1]
            next = f[i + 1]
            if flower == 0 and prev == 0 and next == 0:
                c += 1
                f[i] = 1
        return c >= n


# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


# Example 1:
#
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true


# Example 2:
#
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false


# 1,0,0,0,1

#

res = []

print(res[0])
