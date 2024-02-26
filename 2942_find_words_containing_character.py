class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        index_array = list()
        for i in range(len(words)):
            if x in words[i]:
                index_array.append(i)
        return index_array
