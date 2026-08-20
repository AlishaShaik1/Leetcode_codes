class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        result1=[nums[0]]
        result2=[nums[1]]

        for i in nums[2:]:
            if result1[-1] > result2[-1]:
                result1.append(i)
            else:
                result2.append(i)

        return result1+result2