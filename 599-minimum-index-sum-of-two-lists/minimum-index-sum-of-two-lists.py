class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result=[]
        set1=set(list1)
        set2=set(list2)
        commun=list(set1 & set2)

        dict={}
        for ch in commun:
            dict[ch]=list1.index(ch)+list2.index(ch)
        least=min(dict.values())
        for i in dict:
            if dict[i]==least:
                result.append(i)
        return result
