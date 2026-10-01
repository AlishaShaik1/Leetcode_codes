class Solution:
    def simplifyPath(self,path:str)->str:
        a=[]

        for x in path.split('/'):
            if x=='' or x=='.':
                continue

            if x=='..':
                if a:
                    a.pop()
            else:
                a.append(x)

        return '/'+'/'.join(a)