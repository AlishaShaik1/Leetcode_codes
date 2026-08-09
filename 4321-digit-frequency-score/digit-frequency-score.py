class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        x=[int(i) for i in str(n)]
        x=Counter(x)
        count=0

        for i in x:
            count+=i*x[i]
            
        return count