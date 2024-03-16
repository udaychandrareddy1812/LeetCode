class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = list()
        for i in range(len(nums)):
            x = index[i]
            target.insert(x, nums[i])
        return target
