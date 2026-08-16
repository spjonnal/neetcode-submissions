class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        h_m=defaultdict(list)
        for i in strs:
            key = [0]*26
            for j in i:
                key[ord(j)-ord('a')] += 1
            h_m[tuple(key)].append(i)
        return list(h_m.values())
            
            