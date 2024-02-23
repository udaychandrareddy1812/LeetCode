class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        import math
        answer = list()
        for i in queries:
            count = 0
            for j in points:
                distance = math.sqrt(((i[0]-j[0])**2)+((i[1]-j[1])**2))
                if distance <= i[2]:
                    count = count + 1
            answer.append(count)
        return answer
