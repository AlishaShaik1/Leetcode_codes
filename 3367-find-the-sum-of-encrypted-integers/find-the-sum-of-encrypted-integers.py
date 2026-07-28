class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            x=str(num)

            if len(x)==1:
                result+=int(x)
            else:
                m=[int(i) for i in str(num)]
                n=max(m)
                y=str(n)*len(m)
                result+=int(y)
        return result