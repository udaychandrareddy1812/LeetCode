class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        x = str(n)
        integers = list()
        for i in x:
            integers.append(int(i))
        product = 1
        for i in integers:
            product = product * i
        summ = 0
        for i in integers:
            summ = summ + i
        return (product - summ)
