class Solution(object):
    def pivotIndex(self, nums):
        sums = sum(nums)
        left_sum = 0
        for i, val in enumerate(nums):
            if left_sum == (sums - left_sum - val):
                return i
            left_sum += val
        return -1


print(Solution().pivotIndex([1, 7, 3, 6, 5, 6]))
