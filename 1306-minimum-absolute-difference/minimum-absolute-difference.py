class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min=float('inf')
        result=[]
        for i in range(len(arr)-1):
            diff=arr[i+1]-arr[i]
            if diff<min:
                min=diff

        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==min:
                result.append([arr[i],arr[i+1]])
        
        return result    