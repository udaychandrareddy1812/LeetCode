class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        positive_count = 0
        negative_count = 0
        initial_value = 0
        for i in operations:
            if i == '--X' or i == 'X--':
                negative_count = negative_count + 1
            elif i == '++X' or i == 'X++':
                positive_count = positive_count + 1
        initial_value = initial_value + (positive_count) - (negative_count)
        return initial_value
