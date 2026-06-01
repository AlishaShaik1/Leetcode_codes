class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        sum=0
        cost.sort()
        n=len(cost)-1

        while n>=0:
            sum+=cost[n]
            if n-1>=0:
                sum+=cost[n-1]

            n-=3
        return sum