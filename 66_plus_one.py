class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = ''
        for i in digits:
            x = x + str(i)
        dig = int(x) + 1
        lis = list()
        x = str(dig)
        for i in x:
            lis.append(int(i))
        
        return lis
