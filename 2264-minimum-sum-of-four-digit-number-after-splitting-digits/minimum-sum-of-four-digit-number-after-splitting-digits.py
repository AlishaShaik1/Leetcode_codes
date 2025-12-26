class Solution:
    def minimumSum(self, num: int) -> int:
        s1=str(num)
        s=sorted(s1)
        num1=s[0]+s[2]
        num2=s[1]+s[3]
        return(int(num1)+int(num2))