class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result=[]
        for num in nums:
            x=str(num)
            for ch in x:
                result.append(int(ch))
        return result