class Solution(object):
    def checkTwoChessboards(self,coordinate1,coordinate2):
        return(ord(coordinate1[0])+int(coordinate1[1]))%2==(ord(coordinate2[0])+int(coordinate2[1]))%2