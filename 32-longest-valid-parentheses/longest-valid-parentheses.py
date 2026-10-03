class Solution:
    def longestValidParentheses(self,s:str)->int:
        a=[-1]
        ans=0

        for x in range(len(s)):
            if s[x]=='(':
                a.append(x)
            else:
                a.pop()

                if not a:
                    a.append(x)
                else:
                    ans=max(ans,x-a[-1])

        return ans