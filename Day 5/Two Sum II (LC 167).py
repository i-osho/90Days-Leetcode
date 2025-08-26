class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(numbers):
            if target-num in hashmap:
                return [hashmap[target-num]+1, i+1]
            hashmap[num] = i
        return []