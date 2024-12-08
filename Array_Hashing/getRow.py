class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1]
        for i in range(rowIndex):
            next_row = [0] * (len(res) + 1)
            for j in range(len(res)):
                next_row[j] += res[j]
                next_row[j + 1] += res[j]
            res = next_row

        return res


solution = Solution()

print(solution.getRow(4))

# 119. Pascal's Triangle II

# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

# Solution 1: build the array for pascal triangle
