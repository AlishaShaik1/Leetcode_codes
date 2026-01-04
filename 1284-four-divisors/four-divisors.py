class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        result=0
        for num in nums:
            sum1=0
            count=0
            i=1
            while i*i<=num:
                if num%i==0:
                    d1=i
                    d2=num//i

                    if d1==d2:          
                        count+=1
                        sum1+=d1
                    else:
                        count+=2
                        sum1+=d1+d2

                if count>4:            
                    break
                i += 1
            if count==4:
                result=result+sum1
        return result
