class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # hashmap = {}
        # for i, num in enumerate(nums):
        #     if num in hashmap:
        #         return False
        #     else:
        #         hashmap[num] = i
        # return True
        return len(nums) != len(set(nums))

s1 = Solution()
nums = [1,2,3,2]
s1.containsDuplicate(nums)