class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        positive = None
        if s and s[0] in ['-', '+']:
            if s[0] == '-':
                positive = False
            else:
                positive = True
            s = s[1:]
        elif s and s[0].isdigit():
            positive = True
        if positive is None:
            return 0
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            else:
                break
        if not positive:
            num = -num
        return max(min(num, 2**31 - 1), -2**31)