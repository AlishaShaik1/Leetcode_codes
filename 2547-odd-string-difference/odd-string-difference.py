class Solution:
    def oddString(self, words: List[str]) -> str:
        d={}
        for w in words:
            df=tuple(ord(w[i+1])-ord(w[i])for i in range(len(w)-1))
            d.setdefault(df,[]).append(w)
        for df,lst in d.items():
            if len(lst)==1:return lst[0]