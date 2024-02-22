class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        index_arr = list()
        nums.sort()
        start = 0
        end = len(nums) - 1
        while (start <= end):
            mid = (start + end)//2
            if nums[mid] == target:
                index_arr.append(mid)
                # checking for right indices
                for i in range(mid+1,len(nums)):
                    if nums[i] == target:
                        index_arr.append(i)
                    else:
                        break
                # checking for the left elements:
                for i in range((mid-1),-1,-1):
                    if nums[i] == target:
                        index_arr.append(i)
                    else:
                        break
                break
            elif target < nums[mid]:
                end = mid - 1
            elif target > nums[mid]:
                start = mid + 1
        index_arr.sort()
        return index_arr
