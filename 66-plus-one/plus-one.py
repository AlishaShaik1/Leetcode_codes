class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=int("".join(map(str,digits)))
        num+=1
        result=list(map(int,str(num)))
        return result
        