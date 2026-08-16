class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h_m= {}
        for i in range(len(nums)):
            if nums[i] not in h_m:
                h_m[nums[i]] = 1
            else:
                return True
        return False