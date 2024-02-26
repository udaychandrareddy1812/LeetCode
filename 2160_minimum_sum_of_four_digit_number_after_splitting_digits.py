class Solution:
    def minimumSum(self, num: int) -> int:
        digits = list()
        num = str(num)
        for i in num:
            digits.append(i)
        digits.sort()
        num1 = int(digits[0] + digits[3])
        num2 = int(digits[1] + digits[2])
        return (num1 + num2)
