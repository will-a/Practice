# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    # uses dynamic programming to keep track of the tallest point reached so
    # far going both forward and backward, then adds their overlaps together
    def trap(self, height: list[int]) -> int:
        if len(height) == 0:
            return 0
        fwd = [0] * len(height)
        bwd = [0] * len(height)

        # forward dynamic programming list
        fwd[0] = height[0]
        for i in range(1, len(height)):
            fwd[i] = max(fwd[i-1], height[i])

        # backward dynamic programming list
        bwd[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            bwd[i] = max(bwd[i + 1], height[i])

        # count overlapping tiles and add them to a count
        water = 0
        for i in range(len(height)):
            water += min(fwd[i], bwd[i]) - height[i]
        return water
