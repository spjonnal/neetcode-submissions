class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = float('inf')
        for i in range(len(nums)):
            min_val = min(min_val,nums[i])
        return min_val