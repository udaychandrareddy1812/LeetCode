class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return '0'
        if num<0:
            num = abs(num)
            x = ''
            while(num>0):
                rem = num%7
                div = num//7
                x = x + str(rem)
                num = div
            return '-'+x[::-1]
        elif num>0:
            x = ''
            while(num>0):
                rem = num%7
                div = num//7
                x = x + str(rem)
                num = div
            return x[::-1]
