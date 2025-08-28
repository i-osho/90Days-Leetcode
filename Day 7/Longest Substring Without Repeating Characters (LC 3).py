class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = ""
        length = 0
        for i in s:
            if i not in l:
                l += i
                length = max(length, len(l))
            else:
                l = l[l.index(i) + 1:]
                l += i
        return length
