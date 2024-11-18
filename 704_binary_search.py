class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while(start <= end):
            mid = (start+end)//2
            if nums[mid] == target:
                return nums.index(target)
            elif target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = start + 1
        
        return -1
