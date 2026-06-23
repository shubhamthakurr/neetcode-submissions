class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1]
        for i in range(len(nums)-1):
            prod.append(prod[-1]*nums[i])

        pos_prod = 1
        for i in range(len(prod)-1,-1, -1):
            prod[i] = prod[i] * pos_prod
            pos_prod *= nums[i]

        return prod