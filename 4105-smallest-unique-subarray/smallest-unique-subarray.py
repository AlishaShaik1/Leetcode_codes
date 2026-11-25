class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        BASE=100003
        MOD=10**9 + 7

        def hasUnique(length):
            counts=Counter()
            curr_hash=0
            power=pow(BASE, length-1, MOD)
            for i in range(length):
                curr_hash=(curr_hash * BASE + nums[i]) % MOD
            counts[curr_hash]+=1
            for i in range(length, n):
                left=nums[i-length]
                right=nums[i]
                curr_hash=(curr_hash-left*power) % MOD
                curr_hash=(curr_hash*BASE+right) % MOD
                counts[curr_hash]+=1
            return any(freq==1 for freq in counts.values())
        
        low,high=1,n
        ans=n
        while(low<=high):
            mid=(low+high)//2
            if hasUnique(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans