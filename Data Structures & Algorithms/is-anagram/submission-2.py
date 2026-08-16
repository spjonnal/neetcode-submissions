class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h_s = {}
        h_t = {}
        for i in range(len(s)):
            if s[i] not in h_s:
                h_s[s[i]] = 1
            elif s[i] in h_s:
                h_s[s[i]] += 1
            if t[i] not in h_t:
                h_t[t[i]] = 1
            elif t[i] in h_t:
                h_t[t[i]] += 1
        
        for (i,j) in zip(s,t):
            if i not in h_t or j not in h_s or h_s[i] != h_t[i] or h_s[j] != h_t[j]:
                return False
        return True
        


        