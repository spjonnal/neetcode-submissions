class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_m={}
        for i in range(len(nums)):
            if nums[i] not in h_m:
                h_m[nums[i]] = i
        for i in range(len(nums)):
            res = target - nums[i]
            if res in h_m and i != h_m[res]:
                return [min(i,h_m[res]),max(i,h_m[res])]
        return []