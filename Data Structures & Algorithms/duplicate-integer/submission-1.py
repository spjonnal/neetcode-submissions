class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h_m={}
        for i in range(len(nums)):
            if nums[i] in h_m:
                h_m[nums[i]] += 1
                
            else:
                h_m[nums[i]] = 1
        for key in h_m:
            if h_m[key]>1:
                return True
        return False

