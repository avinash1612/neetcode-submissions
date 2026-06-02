class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        datamap = {}

        for i,n in enumerate(nums):
            diff = target - n
            if diff in datamap:
                return [datamap[diff],i]
            datamap[n]=i
        