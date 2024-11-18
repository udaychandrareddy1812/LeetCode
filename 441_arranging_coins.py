class Solution:
    def arrangeCoins(self, n: int) -> int:
        import math
        dis = (8*n)+1
        x1 = (-1 + math.sqrt(dis))/2
        return int(x1)
