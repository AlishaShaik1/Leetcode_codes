class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        x=set(allowed)
        count=0

        for word in words:
            for i in word:
                if i not in allowed:
                    count+=1
                    break
        return len(words)-count