class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        result=[i for num in nums for i in str(num)]
        
        return result.count(str(digit))