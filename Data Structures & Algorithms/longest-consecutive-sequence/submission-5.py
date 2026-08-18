class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h_m = {}
        n = len(nums)
        for i in range(n):
            h_m[nums[i]] = i
        out = 0
        for i in range(n):
            if nums[i] - 1 not in h_m:
                inner_length = 1
                start = nums[i]
                while start+1 in h_m:
                    inner_length += 1
                    start += 1
                out = max(out,inner_length)
        return out






            

