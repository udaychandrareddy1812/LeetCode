class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        great = 0
        for i in candies:
            if i > great:
                great = i

        result = list()
        for i in candies:
            if ((i + extraCandies) >= great):
                result.append(True)
            else:
                result.append(False)
        return result
