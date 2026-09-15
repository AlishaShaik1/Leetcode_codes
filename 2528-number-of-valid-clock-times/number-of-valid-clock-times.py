class Solution(object):
    def countTime(self, time):
        h1,h2,_,m1,m2=time
        if h1=='?' and h2=='?':h=24
        elif h1=='?':h=3 if ord(h2)<ord('4') else 2
        elif h2=='?':h=4 if h1=='2' else 10
        else:h=1
        if m1=='?' and m2=='?':m=60
        elif m1=='?':m=6
        elif m2=='?':m=10
        else:m=1
        return h*m