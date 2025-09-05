class Solution:
    def romanToInt(self, s: str) -> int:
        rti = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s)):
            total += rti[s[i]]
            if i > 0 and rti[s[i]] > rti[s[i - 1]]:
                total -= 2 * rti[s[i - 1]]
        return total