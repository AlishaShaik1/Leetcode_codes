class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months=[31,28,31,30,31,30,31,31,30,31,30,31]

        def get_date(date):
            month,day=map(int,date.split("-"))
            total=sum(months[:month-1])
            return total+day

        start=max(get_date(arriveAlice),get_date(arriveBob))
        end=min(get_date(leaveAlice),get_date(leaveBob))

        if end<start:
            return 0

        return end-start+1