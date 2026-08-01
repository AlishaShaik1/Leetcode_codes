class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        x=0
        for num in batteryPercentages:
            if num>x:
                x+=1
        return x