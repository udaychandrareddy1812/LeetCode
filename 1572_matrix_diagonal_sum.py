class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        count = 0
        pdia = 0
        sdia = len(mat[0])-1
        for i in mat:
            if (pdia == sdia):
                count = count + i[pdia]
            else:
                count = count + (i[pdia] + i[sdia])
            pdia = pdia + 1
            sdia = sdia - 1
        return count
