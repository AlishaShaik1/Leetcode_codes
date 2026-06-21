class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        i=0
        x=0
        count=0
        costs.sort()
        for cost in costs:
            if coins >= cost:
                coins -= cost
                count += 1
            else:
                break

        return count