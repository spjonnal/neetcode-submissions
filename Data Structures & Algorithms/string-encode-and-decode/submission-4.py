class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for i in strs:
            out += "asdf123"+i
            
        return out

    def decode(self, s: str) -> List[str]:
        encode = str.split(s,'asdf123')[1:]
        return encode
        
