class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t: return ""
        
        ft = {}
        for c in t:
            ft[c] = ft.get(c, 0) + 1
        
        required = len(ft)
        formed = 0
        fs = {}
        l, r = 0, 0
        mins = float("inf")
        start_index = 0
        
        while r < len(s):
            char = s[r]
            fs[char] = fs.get(char, 0) + 1
            
            # Check validity: only increment formed if count matches exactly
            if char in ft and fs[char] == ft[char]:
                formed += 1
            
            # Try to shrink window while valid
            while l <= r and formed == required:
                if (r - l + 1) < mins:
                    mins = r - l + 1
                    start_index = l
                
                # Remove left character
                fs[s[l]] -= 1
                if s[l] in ft and fs[s[l]] < ft[s[l]]:
                    formed -= 1
                l += 1
            
            r += 1
            
        return "" if mins == float("inf") else s[start_index : start_index + mins]