class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x={}

        for string in strs:
            result=''.join(sorted(string))

            if result not in x:
                x[result] = []

            x[result].append(string)

        return list(x.values())