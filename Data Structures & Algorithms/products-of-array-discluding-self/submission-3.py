class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        for i in range(len(nums)-1):
            res.append(res[-1]*nums[i])

        suffix = 1
        for i in range(len(res)-1,-1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res