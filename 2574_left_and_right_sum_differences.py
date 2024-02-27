class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        totalsum = 0
        answer = list()
        for i in nums:
            totalsum = totalsum + i
        leftsum = 0
        rightsum = totalsum
        for i in nums:
            rightsum = rightsum - i
            answer.append(abs(leftsum - rightsum))
            leftsum = leftsum + i
        return answer
