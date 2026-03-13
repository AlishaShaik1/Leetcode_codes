class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        result=[]
        for x in range(0,len(boxes)):
            count=0
            for i in range(0,len(boxes)):
                if boxes[i]=="1":
                    count += abs(i-x)
            result.append(count)
        return result
