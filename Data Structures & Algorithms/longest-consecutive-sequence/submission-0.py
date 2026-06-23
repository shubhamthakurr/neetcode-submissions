class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 not in num_set:
                cur_len = 1
                cur = num + 1
                while cur in num_set:
                    cur_len += 1
                    num_set.remove(cur)
                    cur += 1

                max_len = max(max_len, cur_len)

        return max_len
