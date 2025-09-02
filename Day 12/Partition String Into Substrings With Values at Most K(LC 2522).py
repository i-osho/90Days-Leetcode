class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        count = 0
        current_value = 0
        for char in s:
            digit = int(char)
            if digit > k:
                return -1
            if current_value * 10 + digit > k:
                count += 1
                current_value = digit
            else:
                current_value = current_value * 10 + digit
        if current_value > 0:
            count += 1
        return count