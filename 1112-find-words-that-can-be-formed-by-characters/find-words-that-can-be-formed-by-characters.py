class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result=0
        for ch in words:
            count=0
            x=list(chars)

            for c in ch:
                if c in x:
                    count+=1
                    x.remove(c)
                else:
                    break
                
            if count==len(ch):
                result+=len(ch)
                
        return result
