class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_m = {}
        for i in range(len(nums)):
            if nums[i] in h_m:
                h_m[nums[i]] += 1
            else:
                h_m[nums[i]] = 1
        buc = defaultdict(list)
        for num,freq in h_m.items():
            buc[freq].append(num)
        out = []
        for i in range(len(nums),-1,-1):
            if i in buc:
                out.extend(buc[i])
        return out[:k]
        