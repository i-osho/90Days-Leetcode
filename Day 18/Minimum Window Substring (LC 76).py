class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        left = 0
        min_len = float('inf')
        min_start = 0
        required = len(t_count)
        formed = 0
        window_counts = {}
        
        for right in range(len(s)):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
            
            while left <= right and formed == required:
                char = s[left]
                
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left
                
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1
    
                left += 1
    
        return "" if min_len == float('inf') else s[min_start:min_start + min_len]