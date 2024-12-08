class Solution(object):
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows, 1):
            rows = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    rows.append(1)
                else:
                    rows.append(res[i - 1][j - 1] + res[i - 1][j])

            res.append(rows)

        return res


# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


# 1 -> [1]

# 2 -> [1], [1,1]

# 3 -> [1], [1,1], [1

solution = Solution()

print(solution.generate(5))
