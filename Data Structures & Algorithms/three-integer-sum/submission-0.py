class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = set()
        for i in range(len(sorted_nums)-2):
            l, r = i+1, len(sorted_nums)-1
            target = 0 - sorted_nums[i]

            while(l < r):
                if sorted_nums[l] + sorted_nums[r] > target:
                    r -= 1
                elif sorted_nums[l] + sorted_nums[r] < target:
                    l += 1
                else: 
                    res.add((sorted_nums[i], sorted_nums[l], sorted_nums[r]))
                    r -= 1
                    l += 1
                    
        return list(list(item) for item in res)

