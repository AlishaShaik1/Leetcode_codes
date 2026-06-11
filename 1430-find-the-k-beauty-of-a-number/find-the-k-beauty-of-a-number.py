class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count=0
        n=str(num)

        for i in range(len(n)-k+1):
            x=int(n[i:i+k])
            if x!=0 and num%x==0:
                count+=1
        return count
            