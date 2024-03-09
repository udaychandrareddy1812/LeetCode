class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = list()
        pointer1 = 0
        pointer2 = n
        for i in range(0,n):
            arr.append(nums[i])
            arr.append(nums[n+i])
        return arr
