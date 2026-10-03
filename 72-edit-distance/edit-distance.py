class Solution:
    def minDistance(self,word1:str,word2:str)->int:
        a=len(word2)
        b=list(range(a+1))

        for x in range(1,len(word1)+1):
            c=[x]

            for y in range(1,a+1):
                if word1[x-1]==word2[y-1]:
                    c.append(b[y-1])
                else:
                    c.append(1+min(b[y],c[y-1],b[y-1]))

            b=c

        return b[-1]