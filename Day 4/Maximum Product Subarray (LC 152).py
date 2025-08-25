class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxp = nums[0]
        minp = nums[0]
        p = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = max(num, maxp * num, minp * num)
            minp = min(num, maxp * num, minp * num)
            maxp = temp_max
            p = max(p, maxp)
        
        return p