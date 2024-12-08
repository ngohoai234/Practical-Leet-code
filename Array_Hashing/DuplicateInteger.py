class Solution:
    def hasDuplicate(self, nums) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

# brute force

# outer loop for the 0 -> len(nums)

#   inner loop 0 + 1 -> len(nums)

#       check nums[i] == nums[j]
#             return True
# end of the loop: return False

# class Solution:
#     def hasDuplicate(self, nums) -> bool:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if nums[i] == nums[j]:
#                     return True
#
#         return False


# Space: O(1)
# Time: O(n^2)

# Pros and Cons

# Pros: Easy to implement

# Cons: take a lot of time to check

# better solution
# map or set

# create set data structure

# 1 2 3 1
# |

# []

# 1 2 3 1
#   |
# [1]


# 1 2 3 1
#     |
# [1, 2 ]

# 1 2 3 1

#       |

# [1,2,3]

# Space: O(n)
# Time: O(n)
