class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        x=1
        y=0
        for ch in s:
            w=widths[ord(ch)-ord('a')]
            if y+w>100:
                x+=1
                y=w
            else:
                y+=w
        return [x,y]