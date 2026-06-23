class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        if nums is not None and len(nums) > 0:
            for num in nums:
                if num in seen:
                    return True
                seen.add(num)
        return False