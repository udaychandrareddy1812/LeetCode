class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in grid:
            start = 0
            end = len(i)-1
            while(start <= end):
                mid = (start + end)//2
                if (i[0] < 0):
                    count = count + len(i)
                    break
                if (i[0] == 0):
                    for j in range(len(i)):
                        if i[j] < 0:
                            count = count + (len(i) - j)
                            break
                    break
                if (i[len(i)-1] >= 0):
                    count = count + 0
                    break
                if ((i[mid] < 0) and ((i[mid-1]==0) or (i[mid-1] > 0))):
                    count = count + (len(i) - mid)
                    break
                elif i[mid] >= 0:
                    start = mid + 1
                elif i[mid] < 0:
                    end = mid - 1
        return count
