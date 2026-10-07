class Solution:
    def removeInvalidParentheses(self,s:str)->list[str]:
        def valid(x):
            a=0
            for y in x:
                if y=='(':
                    a+=1
                elif y==')':
                    a-=1
                    if a<0:
                        return False
            return a==0

        a={s}

        while True:
            b=[]

            for x in a:
                if valid(x):
                    b.append(x)

            if b:
                return b

            c=set()

            for x in a:
                for y in range(len(x)):
                    if x[y] in '()':
                        c.add(x[:y]+x[y+1:])

            a=c