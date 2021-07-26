# https://leetcode.com/problems/maximum-subarray/

class Solution:
    # dynamic programming solution that adds to the max subarray if the
    # maximum subarray at the previous array index is greater than zero.
    def maxSubArray(self, nums: list[int]) -> int:
        res = []
        res.append(nums[0])
        maxn = nums[0]

        for i in range(1, len(nums)):
            res.append(nums[i] + max(res[i-1], 0))
            print(res)
            maxn = max(maxn, res[i])
        return maxn


s = Solution()
s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
