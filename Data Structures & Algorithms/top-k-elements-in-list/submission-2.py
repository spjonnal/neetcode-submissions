class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_m = {}
        for i in range(len(nums)):
            if nums[i] not in h_m:
                h_m[nums[i]] = 1
            else:
                h_m[nums[i]] += 1
        buc = defaultdict(list)
        for key,count in h_m.items():
            buc[count].append(key)
        out = []
        print(buc)
        for i in range(len(nums),0,-1):
            
            if i in buc:
                out.extend(buc[i])
                
        if len(out)>=k:
            return out[:k]
        else:
            return out

