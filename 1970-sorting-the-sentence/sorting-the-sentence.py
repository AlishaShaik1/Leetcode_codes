class Solution:
    def sortSentence(self, s: str) -> str:
        dic={}
        for ch in s.split():
            x=ch[-1]
            ch1=ch[:-1]
            dic[x]=ch1
        sorted_dic=dict(sorted(dic.items()))

        result=" ".join(sorted_dic.values())

        return result