class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums=[num for num in nums if num%2==0]
        if not nums:
            return -1
        
        freq=Counter(nums)
        x=max(freq.values())
        result=min(num for num in freq if freq[num]==x)
        return result
        
        