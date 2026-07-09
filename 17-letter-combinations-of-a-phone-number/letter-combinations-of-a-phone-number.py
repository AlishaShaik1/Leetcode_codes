class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result=[0,0,["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
        temp=[]
        for i in range(len(digits)):
            x=int(digits[i])
            temp.append(result[x])

        ans=product(*temp)

        return ["".join(x) for x in ans]




        
