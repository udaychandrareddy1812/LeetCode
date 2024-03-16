class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decomp = list()
        count = 0
        while (count < len(nums)):
            x = nums[count]
            for i in range(x):
                decomp.append(nums[count+1])
            count = count + 2
        return decomp
