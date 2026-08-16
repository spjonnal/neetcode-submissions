class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h_m1={}
        h_m2={}
        for i in range(len(t)):
            if s[i] not in h_m1:
                h_m1[s[i]] = 1
            else:
                h_m1[s[i]] += 1
            if t[i] not in h_m2:
                h_m2[t[i]] = 1
            else:
                h_m2[t[i]] += 1
        
        for i in h_m1:
            if i not in h_m1 or i not in h_m2 or h_m1[i] != h_m2[i]:
                return False
        return True





        