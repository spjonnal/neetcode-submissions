class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        n = len(nums)
        h = n-1
        min_val = float('inf')
        while(l<=h):
            mid = (l+h)//2
            min_val = min(min_val,nums[mid])
            if nums[mid] < nums[h]:
                h = mid-1
            else:
                l = mid+1
        return min_val