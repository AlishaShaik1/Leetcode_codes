class Solution:
    def gameOfLife(self,board:list[list[int]])->None:
        m=len(board)
        n=len(board[0])

        for x in range(m):
            for y in range(n):
                a=0

                for i in range(max(0,x-1),min(m,x+2)):
                    for j in range(max(0,y-1),min(n,y+2)):
                        if board[i][j]&1:
                            a+=1

                if board[x][y]==1:
                    a-=1

                    if a==2 or a==3:
                        board[x][y]|=2
                elif a==3:
                    board[x][y]|=2

        for x in range(m):
            for y in range(n):
                board[x][y]>>=1