class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = list()
        for i in range(0,len(nums)):
            ans.append(nums[nums[i]])
        return ans
