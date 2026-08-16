class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        h_m={}    
        for i in range(len(nums)):
            h_m[nums[i]] = i
        for i in range(len(nums)):
            y = target - nums[i]
            if  y in h_m and i != h_m[y]:
                if i < h_m[y]:
                    out.append(i)
                    out.append(h_m[y])
                    break
                else:
                    out.append(h_m[y])
                    out.append(i)
                    break
        return out