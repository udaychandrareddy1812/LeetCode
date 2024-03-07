class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        #element_sum
        element_sum = 0
        for i in nums:
            element_sum = element_sum + i
        
        #digit sum
        digit_sum = 0
        for i in nums:
            i = str(i)
            for j in i:
                digit_sum = digit_sum + int(j)
        
        return abs(element_sum - digit_sum)
