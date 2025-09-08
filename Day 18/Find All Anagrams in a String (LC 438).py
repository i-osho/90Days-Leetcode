class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        
        len_p = len(p)
        count_p = Counter(p)
        count_s = Counter()
        
        result = []
        
        for i in range(len(s)):
            count_s[s[i]] += 1
            
            if i >= len_p:
                if count_s[s[i - len_p]] == 1:
                    del count_s[s[i - len_p]]
                else:
                    count_s[s[i - len_p]] -= 1
            
            if count_s == count_p:
                result.append(i - len_p + 1)
        
        return result