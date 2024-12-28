class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        del1 = points[0][0]*(points[1][1]-points[2][1])
        del2 = points[1][0]*(points[2][1]-points[0][1])
        del3 = points[2][0]*(points[0][1]-points[1][1])
        delt = del1 + del2 + del3
        if delt != 0:
            return True
        elif delt == 0:
            return False
