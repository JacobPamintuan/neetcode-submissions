class Solution:

    def encode(self, strs: List[str]) -> str:
    
        encoded = ""

        for s in strs:
            encoded += str(len(s)) + "#" + s

        return encoded

    def decode(self, s: str) -> List[str]:
        i,j = 0, 0
        ans = []

        while j < len(s):
            if s[j] == '#':
                length = int(s[i:j])
                ans.append(s[j+1:j+1+length])
                i = j = j+1+length

            else:
                j+=1

        return ans

        

