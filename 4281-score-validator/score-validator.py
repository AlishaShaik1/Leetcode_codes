class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score,counter=0,0
        nums=["0","1","2","3","4","6"]

        for ch in events:
            if ch in nums:
                score+=int(ch)
            elif ch=="W":
                counter+=1
            elif ch=="WD" or "NB":
                score+=1
            else:
                score+=1
            if counter>=10:
                break
        return [score,counter]