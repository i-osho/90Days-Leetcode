class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = nums[:]
        n = len(arr)
        for i in range(n):
            arr[(i+k) % n] = nums[i]
        for i in range(n):
            nums[i] = arr[i]
    

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        m = k % len(nums)
        if len(nums) == 1 or m == 0:
            return
        nums[:] = nums[-m:] + nums[:len(nums) - m]