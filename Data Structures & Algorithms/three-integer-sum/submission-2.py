class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []
        for i in range(len(sorted_nums)-2):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            l, r = i+1, len(sorted_nums)-1
            while l < r:
                threesum = sorted_nums[i] + sorted_nums[l] + sorted_nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else: 
                    res.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    r -= 1
                    l += 1
                    while l < r and sorted_nums[l] == sorted_nums[l-1]:
                        l += 1
                    
        return res