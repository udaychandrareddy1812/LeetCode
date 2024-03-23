class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acr = ''
        for i in words:
            acr = acr + i[0]
        if acr == s:
            return True
        else:
            return False
