class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result=set()
        for x,y,z in permutations(digits,3):
            if x!=0 and z&1==0:
                result.add(100*x + 10*y + z)
        return sorted(result)