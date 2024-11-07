class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        one_count = 0
        large = 0
        for i in nums:
            if i == 0:
                if one_count>large:
                    large = one_count
                one_count = 0
            if i == 1:
                one_count = one_count + 1
        if one_count>large:
            large = one_count
        return large
