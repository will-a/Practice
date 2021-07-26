# https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution:
    # in each iteration, check which side of the rotation the mid pointer is
    # on. if on the wrong side, move the appropriate l or r value one index
    # towards the appropriate side. if on the right side, perform a normal
    # binary search.
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        mid = (l + r) // 2

        while l <= r:
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            mid = (l + r) // 2
        return -1
