class Solution:
    def isValid(self, s: str) -> bool:
        h_m = {}
        h_m['('] = ')'
        h_m['{'] = '}'
        h_m['['] = ']'
        st  = []
        n = len(s)
        for i in range(n):
            if s[i] not in [')','}',']']:
                st.append(s[i])
                
            else:
                if st:
                    var = st.pop()
                    
                    if h_m[var] != s[i]:
                        return False
                else:
                    return False
                
        return len(st)<=0