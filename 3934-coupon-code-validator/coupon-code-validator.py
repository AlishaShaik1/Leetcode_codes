class Solution(object):
    def validateCoupons(self,code,businessLine,isActive):
        p={"electronics":0,"grocery":1,"pharmacy":2,"restaurant":3}
        v=[]
        for c,b,a in zip(code,businessLine,isActive):
            if a and b in p and c and all(ch.isalnum() or ch=='_' for ch in c):
                v.append((p[b],c))
        v.sort(key=lambda x:(x[0],x[1]))
        return [c for _,c in v]