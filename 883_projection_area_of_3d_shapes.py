class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        
        # xy plane projection
        xy_count = 0
        for i in grid:
            for j in i:
                if j!=0:
                    xy_count = xy_count + 1

        # xz plane projection
        xz_count = 0
        for i in grid:
            xz_count = xz_count + max(i)

        # yz plane projection
        yz_count = 0
        count = 0
        for i in range(0,len(grid)):
            yzlis = list()
            for j in range(0,len(grid)):
                yzlis.append(grid[j][i])
            yz_count = yz_count + max(yzlis)
        
        total_count = xy_count + xz_count + yz_count

        return total_count
