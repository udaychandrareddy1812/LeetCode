class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        one_count = list()
        for i in bank:
            one = 0
            for j in i:
                if j == '1':
                    one = one + 1
            if one > 0:
                one_count.append(one)
        beam_count = 0
        n,r = 0,0
        for i in range(0,(len(one_count)-1)):
            n = one_count[i]
            r = one_count[i+1]
            beam_count = beam_count + (n * r)
        return beam_count
