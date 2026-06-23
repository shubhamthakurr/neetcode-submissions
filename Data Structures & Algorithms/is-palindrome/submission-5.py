class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        lower_str = s.lower()
        def isAlphanumeric(c):
            if ord("z") >= ord(c) >= ord("a") or ord("9") >= ord(c) >= ord("0"):
                return True
            else:
                return False

        while l < r and l < len(s) and r >= 0:
            while l < len(s) and isAlphanumeric(lower_str[l]) is False:
                l += 1
            while r >= 0 and isAlphanumeric(lower_str[r]) is False:
                r -= 1

            if(l <= r and lower_str[l] == lower_str[r]): 
                l += 1
                r -= 1
            elif l > r:
                return True
            else:
                return False
        return True



        