class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        msum = float('-inf')
        i = 0
        j = k
        csum = sum(nums[i:j])

        while j < len(nums):
            msum = max(msum, csum)
            csum -= nums[i]
            csum += nums[j]
            i += 1
            j += 1
        return max(msum, csum) / k
