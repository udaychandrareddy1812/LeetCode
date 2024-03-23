class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        y = s.split()
        y = y[:k]
        z = ''
        for i in y:
            z = z + i + ' '
        return z.rstrip()
