class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxSub = 0
        uniq = set()
        while r < len(s):
            while s[r] in uniq:
                uniq.remove(s[l])
                l += 1
            uniq.add(s[r])
            r += 1

            maxSub = max(maxSub, r - l)

        return maxSub