class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        elif len(arr)>=3:
            big = arr[0]
            for i in arr:
                if i>big:
                    big=i
            x = arr.index(big)
            print(x)
            # strictly increasing
            up = 0
            for i in range(0,x):
                if arr[i]>=arr[i+1]:
                    up = up + 1

            # strictly decreasing
            down = 0
            for i in range(x,len(arr)-1):
                if arr[i]<=arr[i+1]:
                    down = down + 1
            
            if (up==0 and down==0) and (x!=0 and (len(arr)-x)>1):
                return True
            else:
                return False
