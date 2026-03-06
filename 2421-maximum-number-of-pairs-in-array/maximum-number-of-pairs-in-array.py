class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        result=sum(x//2 for x in Counter(nums).values())
        return [result,len(nums)-2*result]