class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        num = str(num)
        if len(num) == 1:
            return True
        elif len(num) > 1:
            rev1 = num[::-1]
            rev1 = rev1.lstrip('0')
            rev2 = rev1[::-1]

            if num == rev2:
                return True
            else:
                return False
