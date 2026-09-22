from collections import Counter
class Solution(object):
    def rearrangeCharacters(self,s,target):
        sc=Counter(s)
        tc=Counter(target)
        return min(sc[c]//tc[c] for c in tc)