class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        x=[-1]*26

        for i in range(len(s)):
            ch=ord(s[i])-ord('a')
            if x[ch]==-1:
                x[ch]=i
            else:
                y=i-x[ch]-1

                if y!=distance[ch]:
                    return False

        return True