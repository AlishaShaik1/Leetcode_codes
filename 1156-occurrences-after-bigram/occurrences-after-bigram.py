class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        s=text.split()
        result=[]
        
        for i in range(len(s)-2):
            if s[i]==first and s[i+1]==second:
                result.append(s[i+2])
        
        return result