class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        count=0
        result=[i for num in nums for i in str(num)]
        for ch in result:
            if ch==str(digit):
                count+=1
        return count