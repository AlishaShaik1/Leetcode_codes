class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums=sorted(set(arr))

        result= {num:i+1 for i,num in enumerate(nums)}
        return [result[num] for num in arr]
