class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_m = defaultdict(list)
        for i in range(len(strs)):
            count = [0]*26 # to count character freqency

            for j in strs[i]:
                count[ord(j) - ord("a")] += 1
            h_m[tuple(count)].append(strs[i])
        return list(h_m.values())