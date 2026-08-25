class Solution:
    def isValid(self, s: str) -> bool:
        h_m = {}
        h_m[')'] = '('
        h_m[ '}'] = '{'
        h_m[']'] = '['
        st  = []
        n = len(s)
        for i in range(n):
            if s[i] not in h_m:
                st.append(s[i])
            else:
                if not st  or (st and h_m[s[i]] != st.pop()):
                    return False
        return len(st)<=0
