class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        result1=[]
        result2=[]
        result3=[]

        for i in range(len(nums)):
            if nums[i]==pivot:
                result1.append(nums[i])
            elif nums[i]>pivot:
                result2.append(nums[i])
            else:
                result3.append(nums[i])

        return result3+result1+result2
