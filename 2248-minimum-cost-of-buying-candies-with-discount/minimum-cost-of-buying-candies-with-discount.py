class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        sum=0
        cost.sort(reverse=True)
        n=len(cost)
        for i in range(n):
            if i%3==2:
                continue
            sum=sum+cost[i]
        return sum
            

        