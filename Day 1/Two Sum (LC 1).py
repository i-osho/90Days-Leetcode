# Two Sum (LC 1)
class Solution:
    def twoSum(self, nums: list[int], target: int):
        hashmap={}
        for i, num in enumerate(nums):
            j = target-num
            if j in hashmap:
                return [hashmap[j],i]
            hashmap[num] = i
        return []

sol = Solution()
nums = [2, 17, 11, 15,7]
target = 9
print(sol.twoSum(nums, target))


