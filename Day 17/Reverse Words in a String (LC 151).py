class Solution:
    def reverseWords(self, s: str) -> str:
        s.lstrip()
        s.rstrip()
        s_list = s.split()
        s_list.reverse()
        return ' '.join(s_list)