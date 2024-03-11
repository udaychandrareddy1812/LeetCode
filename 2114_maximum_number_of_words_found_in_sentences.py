class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi = 0
        for i in sentences:
            length = len(i.split())
            if length > maxi:
                maxi = length
        return maxi
