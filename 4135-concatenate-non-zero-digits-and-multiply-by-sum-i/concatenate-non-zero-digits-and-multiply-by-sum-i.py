class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=0
        nums=str(n)
        result=""
        for ch in nums:
            if ch!="0":
                result+=ch
                x+=int(ch)

        if result == "":
            return 0
            
        return int(result) *x

