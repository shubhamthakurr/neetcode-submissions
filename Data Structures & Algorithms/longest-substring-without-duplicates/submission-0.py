class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxSub = 0
        uniq = set()
        while r < len(s):
            if s[r] not in uniq:
                uniq.add(s[r])
                r += 1
            else: 
                while s[r] in uniq:
                    uniq.remove(s[l])
                    l += 1

            maxSub = max(maxSub, r - l)

        return maxSub