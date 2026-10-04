class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = {}
        for ch in t:
            count[ch] = 1 + count.get(ch, 0)

        charSet = set(count.keys())
        l = 0
        res = s+"#"

        for r in range(len(s)):
            if s[r] in count: 
                count[s[r]] -= 1
                if count[s[r]] == 0: 
                    charSet.remove(s[r])
            
            while not charSet:
                if len(res) > len(s[l:r+1]):
                    res = s[l:r+1]
                if s[l] in count:
                    count[s[l]] +=1
                    if count[s[l]] > 0:
                        charSet.add(s[l])
                l += 1

        if len(res) > len(s): return ""
        return res

            
