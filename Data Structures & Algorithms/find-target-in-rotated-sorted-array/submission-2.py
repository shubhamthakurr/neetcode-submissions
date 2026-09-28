class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)

        if nums[pivot] <= target <= nums[-1]:
            return self.binary_search(nums, pivot, len(nums) - 1, target)

        return self.binary_search(nums, 0, pivot - 1, target)

    def find_pivot(self, nums):
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid

        return lo

    def binary_search(self, nums, lo, hi, target):
        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1