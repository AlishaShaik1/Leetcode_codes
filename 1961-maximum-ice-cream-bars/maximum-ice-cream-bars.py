class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        i=0
        x=0
        count=0
        costs.sort()
        while i<len(costs) and x+costs[i]<=coins:
            x+=costs[i]
            count+=1
            i+=1
        return count