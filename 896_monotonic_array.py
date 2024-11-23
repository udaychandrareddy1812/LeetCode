class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if (len(nums)==1) or (len(nums)==2):
            return True
        elif (len(nums)>=3):
            if nums[0]<=nums[len(nums)-1]:
                for i in range(0,len(nums)-1):
                    if nums[i]<=nums[i+1]:
                        continue
                    else:
                        return False
                if nums[i]<=nums[i+1]:
                    return True
                else:
                    return False
            elif nums[0]>=nums[len(nums)-1]:
                for i in range(0,len(nums)-1):
                    if nums[i]>=nums[i+1]:
                        continue
                    else:
                        return False
                if nums[i]>=nums[i+1]:
                    return True
                else:
                    return False
