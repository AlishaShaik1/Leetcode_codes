
class Solution:
    def removeDuplicateLetters(self,s:str)->str:
        a=[]
        b=set()
        c={x:s.count(x) for x in s}

        for x in s:
            c[x]-=1

            if x in b:
                continue

            while a and a[-1]>x and c[a[-1]]>0:
                b.remove(a.pop())

            a.append(x)
            b.add(x)

        return ''.join(a)