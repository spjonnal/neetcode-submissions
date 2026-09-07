class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums)-1
        out = float('inf')
        while l <= h:
            mid = (l+h)//2
            out = min(out,nums[mid])
            if nums[l] < nums[mid] and nums[mid] < nums[h]:
                h = mid-1
            elif nums[l] > nums[mid] and nums[mid] > nums[h]:
                l = mid+1
            elif nums[l] > nums[mid] and nums[mid] < nums[h]:
                h = mid-1
            else:
                l = mid+1
        return out