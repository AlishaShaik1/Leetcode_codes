class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=set()
        for i in range(len(nums)+1):
            for p in permutations(nums,i):
                result.add(tuple(sorted(p)))
        return [list(s) for s in result]