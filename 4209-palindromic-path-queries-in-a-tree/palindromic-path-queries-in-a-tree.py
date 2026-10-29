class Solution:
    def palindromePath(self,n:int,edges:list[list[int]],s:str,queries:list[str])->list[bool]:
        g=[[] for _ in range(n)]
        for x,y in edges:
            g[x].append(y)
            g[y].append(x)

        a=[-1]*n
        b=[0]*n
        a[0]=0
        c=[0]
        d=[]

        while c:
            x=c.pop()
            d.append(x)
            for y in g[x]:
                if y!=a[x]:
                    a[y]=x
                    b[y]=b[x]+1
                    c.append(y)

        tin=[0]*n
        size=[1]*n
        for x,y in enumerate(d):
            tin[y]=x

        for x in d[::-1]:
            if x:
                size[a[x]]+=size[x]

        tout=[tin[x]+size[x]-1 for x in range(n)]

        log=n.bit_length()
        up=[a[:]]
        for x in range(1,log):
            up.append([up[x-1][up[x-1][y]] for y in range(n)])

        def lca(x,y):
            if b[x]<b[y]:
                x,y=y,x
            z=b[x]-b[y]
            for i in range(log):
                if z>>i&1:
                    x=up[i][x]
            if x==y:
                return x
            for i in range(log-1,-1,-1):
                if up[i][x]!=up[i][y]:
                    x=up[i][x]
                    y=up[i][y]
            return a[x]

        def bit(x):
            return 1<<(ord(x)-97)

        f=[0]*(n+2)

        def add(x,v):
            while x<=n:
                f[x]^=v
                x+=x&-x

        def get(x):
            z=0
            while x:
                z^=f[x]
                x-=x&-x
            return z

        def update(x,v):
            add(tin[x]+1,v)
            add(tout[x]+2,v)

        t=[bit(x) for x in s]
        p=[0]*n
        for x in d:
            p[x]=t[x] if x==0 else p[a[x]]^t[x]

        ans=[]

        for q in queries:
            z=q.split()
            if z[0]=='update':
                x=int(z[1])
                y=bit(z[2])
                update(x,t[x]^y)
                t[x]=y
            else:
                x=int(z[1])
                y=int(z[2])
                z=lca(x,y)
                v=(p[x]^get(tin[x]+1))^(p[y]^get(tin[y]+1))^t[z]
                ans.append(v&(v-1)==0)

        return ans