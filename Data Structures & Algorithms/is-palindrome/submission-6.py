class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        i = 0
        n = len(s)
        j = n-1
        while i <= j:
            while i <n and not s[i].isalnum():
                i += 1
            while j >-1 and not s[j].isalnum():
                j -= 1
            if i < n and j >-1 and s[i].isalnum() and s[j].isalnum() and s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True