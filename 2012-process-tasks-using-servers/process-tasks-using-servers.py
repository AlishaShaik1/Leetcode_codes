import heapq

class Solution:
    def assignTasks(self,servers:list[int],tasks:list[int])->list[int]:
        a=[]
        b=[]

        for i in range(len(servers)):
            heapq.heappush(a,(servers[i],i))

        ans=[]
        time=0

        for i in range(len(tasks)):
            time=max(time,i)

            while b and b[0][0]<=time:
                t,w,j=heapq.heappop(b)
                heapq.heappush(a,(w,j))

            if not a:
                time=b[0][0]

                while b and b[0][0]<=time:
                    t,w,j=heapq.heappop(b)
                    heapq.heappush(a,(w,j))

            w,j=heapq.heappop(a)
            ans.append(j)

            heapq.heappush(b,(time+tasks[i],w,j))

        return ans