class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        # sum of integers that are not divisible by m
        num2 = (m * ((math.floor(n/m)) * ((math.floor(n/m)) + 1))/2)
        # sum of integers that are divisible by m
        num1 = (n*((n+1)/2)) - num2
        return (int(num1 - num2))
