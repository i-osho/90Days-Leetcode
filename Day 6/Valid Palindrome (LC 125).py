import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        rev = ""
        for i in s:
            if i.isalnum():
                rev += i.lower()
            else: continue
        print(s,rev[::-1])
        return rev == rev[::-1]