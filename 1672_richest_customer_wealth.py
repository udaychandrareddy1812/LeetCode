class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        rich = 0
        for i in accounts:
            sum = 0
            for j in i:
                sum = sum + j
            if sum >= rich:
                rich = sum
        return rich
