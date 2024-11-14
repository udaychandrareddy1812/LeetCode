class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            x = len(i)-1
            if target>=i[0] and target<=i[x]:
                start = 0
                end = len(i) - 1
                while(start <= end):
                    mid = (start + end)//2
                    if i[mid] == target:
                        return True
                    elif target < i[mid]:
                        end = mid - 1
                    elif target > i[mid]:
                        start = mid + 1 
        return False
