class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1str = ''
        for i in word1:
            word1str = word1str + i

        word2str = ''
        for i in word2:
            word2str = word2str + i

        if (word2str == word1str):
            return True
        else:
            return False
