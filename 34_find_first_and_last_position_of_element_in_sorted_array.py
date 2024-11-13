class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        count = 0
        while(start <= end):
            mid = (start + end)//2

            if nums[mid] == target:
                x = mid
                y = mid
                print(mid)
                for i in range(mid+1,len(nums)):
                    if nums[i] == target:
                        x = x + 1
                    else:
                        break
                for i in range(mid-1,-1,-1):
                    if nums[i] == target:
                        y = y - 1 
                    else:
                        break
                return [y,x]
            elif target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
        
        return [-1,-1]
