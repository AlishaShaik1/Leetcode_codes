class Solution(object):
    def isCircularSentence(self,sentence):
        if sentence[0]!=sentence[-1]:
            return False
        for i in range(len(sentence)):
            if sentence[i]==' ' and sentence[i-1]!=sentence[i+1]:
                return False
        return True