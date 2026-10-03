class Solution:
    def wordBreak(self,s:str,wordDict:list[str])->bool:
        a=set(wordDict)
        b=[False]*(len(s)+1)
        b[0]=True

        for x in range(1,len(s)+1):
            for y in range(x):
                if b[y] and s[y:x] in a:
                    b[x]=True
                    break

        return b[-1]